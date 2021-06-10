from django.shortcuts import render, redirect, reverse
from django.views.generic import View, ListView, DetailView
from django.http.response import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import F

from comments.forms import CommentForm
from .models import Genre, Book, Cycle, Library, Like
from comments.models import Comment
from chapters.models import Chapter
from .forms import CycleForm, BookForm


class ShowCaseBookList(ListView):
    template_name = 'homepage.html'
    context_object_name = 'books'
    model = Book

    def get_queryset(self, *args, **kwargs):
        books = Book.objects.all()
        return books


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'book_list'


class BookListByGenreView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'book_list'

    def get_queryset(self, *args, **kwargs):
        queryset = Book.objects.all().filter(genre__slug=self.kwargs.get('slug'))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookListByGenreView, self).get_context_data(**kwargs)
        context['listed_by_genre'] = True
        context['genre'] = Genre.objects.get(slug=self.kwargs.get('slug'))
        return context


class BookDetailView(View):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        Book.objects.filter(id=id).update(views=F("views") + 1)
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


class AddBookView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = BookForm()
        context = {
            'form': form
        }
        return render(request, 'books/book_form.html', context)

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

        return render(request, 'books/update_book_form.html', context)

    def post(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)
        if book.author != request.user:
            return redirect(reverse('books:detail', args=[book.id]))
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
        return redirect(reverse('books:update_book', args=[book.id]))


class UpdateBookTextView(View):
    def get(self, request, id, *args, **kwargs):
        book = get_object_or_404(Book, id=id, author=request.user)
        context = {
            'book': book
        }
        return render(request, 'books/update_book_text.html', context)


class DeleteCycleView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, author=request.user, id=book_id)
        book.delete()
        return redirect(reverse('authors:author_books'))


class AddCycleView(View):
    def get(self, request, *args, **kwargs):
        form = CycleForm()
        context = {
            'form': form
        }
        return render(request, 'books/cycle_form.html', context)

    def post(self, request, *args, **kwargs):
        form = CycleForm(request.POST)
        if form.is_valid():
            cycle = form.save(commit=False)
            cycle.creator = request.user
            cycle.save()
            return redirect('authors:authors_cycles')

        return redirect('authors:authors_cycles')


@login_required
@require_POST
def delete_cycle(request, id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        cycle = get_object_or_404(Cycle, id=id)
        if cycle.creator == request.user:
            cycle.delete()
            return JsonResponse({'success': True, 'id': id}, status=200)
        return JsonResponse({'success': True}, status=401)


class EditCycleView(View):
    def get(self, request, id):
        cycle = get_object_or_404(Cycle, id=id, creator=request.user)
        cycle_form = CycleForm(instance=cycle)
        context = {
            'form': cycle_form,
            'cycle': cycle
        }
        return render(request, 'books/update_cycle_form.html', context)

    def post(self, request, id):
        cycle = get_object_or_404(Cycle, id=id, creator=request.user)
        cycle_form = CycleForm(request.POST, instance=cycle)

        if cycle_form.is_valid():
            cycle_form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False})


class CycleDetailView(DetailView):
    model = Cycle
    template_name = 'books/cycle_detail.html'
    context_object_name = 'cycle'


@require_POST
@login_required
def add_to_library(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        library, created = Library.objects.get_or_create(user=request.user)
        if Library.objects.filter(user=request.user, books=book).exists():
            library.books.remove(book)
            message = "Deleted"
        else:
            library.books.add(book)
            message = "Added"
        return JsonResponse({'success': True, 'message': message})


@require_POST
@login_required
def add_like_to_book(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        like, created = Like.objects.get_or_create(user=request.user, book=book)
        if not created:
            like.delete()
        likes_count = book.get_likes_count
        return JsonResponse({'success': True, 'likes': likes_count})