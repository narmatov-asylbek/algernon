from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http.response import JsonResponse

from .forms import ChapterForm
from .models import Chapter
from books.models import Book


class AddChapterView(LoginRequiredMixin, View):
    """ View for adding a new chapter """
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id, author=request.user)
        form = ChapterForm()
        context = {
            'book_id': book.id,
            'form': form
        }
        return render(request, 'chapters/chapter_form.html', context)

    def post(self, request, book_id):
        form = ChapterForm(request.POST, request.FILES)
        if form.is_valid():
            book = get_object_or_404(Book, id=book_id)
            title = form.cleaned_data.get('title')
            text = form.cleaned_data.get('text')
            author = request.user
            Chapter.objects.create(book=book, title=title, text=text, author=author)
            return redirect(reverse('books:update_book_content', args=[book_id]))


class UpdateChapterView(View):
    """ View for updating chapter's text """
    def get(self, request, book_id, id):
        chapter = Chapter.objects.get(book_id=book_id, id=id, author=request.user)
        form = ChapterForm(instance=chapter)
        context = {
            'form': form
        }
        return render(request, 'chapters/chapter_form.html', context)

    def post(self, request, book_id, id):
        chapter = Chapter.objects.get(book_id=book_id, id=id, author=request.user)
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return render(request, 'chapters/chapter_form.html', {'form': form})


@login_required
@require_POST
def delete_chapter(request, book_id, chapter_id):
    """ Dynamically deleting chapter """
    chapter = get_object_or_404(Chapter, book_id=book_id, id=chapter_id)
    chapter.delete()
    return JsonResponse({'success': True, 'id': chapter_id}, status=200)