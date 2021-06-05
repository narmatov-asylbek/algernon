from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View

from .forms import AddChapterForm
from .models import Chapter
from books.models import Book


class AddChapterView(View):
    def get(self, request, *args, **kwargs):
        form = AddChapterForm()
        context = {
            'form': form
        }
        return render(request, 'chapters/chapter_form.html', context)

    def post(self, request, book_id):
        form = AddChapterForm(request.POST)

        if form.is_valid():
            book = get_object_or_404(Book, id=book_id)
            title = form.cleaned_data.get('title')
            text = form.cleaned_data.get('text')
            author = request.user
            Chapter.objects.create(book=book, title=title, text=text, author=author)
            return redirect(reverse('books:detail', args=[book_id]))
