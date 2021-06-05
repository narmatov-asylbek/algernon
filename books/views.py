from django.shortcuts import render, redirect, reverse
from django.views.generic import View, ListView
from django.http.response import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from comments.forms import CommentForm
from .models import Genre, Book, Cycle
from comments.models import Comment
from chapters.models import Chapter
from .forms import CycleForm, BookForm
from chapters.forms import AddChapterForm


class BookList(ListView):
    template_name = 'homepage.html'
    context_object_name = 'books'
    model = Book

    def get_queryset(self, *args, **kwargs):
        try:
            slug = self.kwargs['slug']
            genre = get_object_or_404(Genre, slug=slug)
            books = Book.objects.filter(genre=genre)
        except:
            books = Book.objects.all()
        return books

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.filter(is_important=True)[:3]
        return context


class BookDetailView(View):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        chapters = Chapter.objects.filter(book=book)
        comments = Comment.objects.filter(book=book)
        comment_form = CommentForm()
        context = {
            'book': book,
            'chapters': chapters,
            'comments': comments,
            'comment_form': comment_form
        }
        return render(request, 'books/book_detail.html', context)

    def post(self, request, id):
        book = get_object_or_404(Book, id=id)
        author = request.user
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.cleaned_data.get('comment_text')
            reply_obj = None
            try:
                reply_id = int(request.POST.get('reply_id'))
            except:
                reply_id = None
            if reply_id:
                reply_obj = Comment.objects.get(id=reply_id)
            if reply_obj:
                Comment.objects.create(book=book, user=author, parent=reply_obj, comment_text=comment)
            else:
                Comment.objects.create(book=book, user=author, comment_text=comment)
            return redirect(reverse('books:detail', args=[book.id]))


class AddBookView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = BookForm()
        context = {
            'form': form
        }
        return render(request, 'authors/books/book_form.html', context)

    def post(self, request, *args, **kwargs):
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.save()
            return redirect('books:detail', book.id)


class UpdateBookSettings(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)
        if book.author != request.user:
            return redirect(reverse('books:detail', args=[book.id]))
        form = BookForm(instance=book)

        context = {
            'form': form,
            'book': book,
            'active': True
        }

        return render(request, 'authors/books/update_book_form.html', context)

    def post(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)
        if book.author != request.user:
            return redirect(reverse('books:detail', args=[book.id]))
        form = BookForm(request.POST, request.FILES, instance=book)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False})


class UpdateBookTextView(View):
    def get(self, request, id, *args, **kwargs):
        book = get_object_or_404(Book, id=id, author=request.user)
        context = {
            'book': book
        }
        return render(request, 'authors/books/update_book_text.html', context)

class AddCycleView(View):
    def get(self, request, *args, **kwargs):
        form = CycleForm()
        context = {
            'form': form
        }
        return render(request, 'authors/books/cycle_form.html', context)

    def post(self, request, *args, **kwargs):
        form = CycleForm(request.POST)
        if form.is_valid():
            cycle = form.save(commit=False)
            cycle.creator = request.user
            cycle.save()
            return redirect('authors:authors_cycles')

        return redirect('authors:authors_cycles')


class DeleteCycleView(View):
    def post(self, request, id):
        cycle = get_object_or_404(Cycle, id=id, creator=request.user)
        cycle.delete()
        return JsonResponse({'success': True})


class EditCycleView(View):
    def get(self, request, id):
        cycle = get_object_or_404(Cycle, id=id, creator=request.user)
        cycle_form = CycleForm(instance=cycle)
        context = {
            'form': cycle_form,
            'cycle': cycle
        }
        return render(request, 'authors/books/update_cycle_form.html', context)

    def post(self, request, id):
        cycle = get_object_or_404(Cycle, id=id, creator=request.user)
        cycle_form = CycleForm(request.POST, instance=cycle)

        if cycle_form.is_valid():
            cycle_form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False})
