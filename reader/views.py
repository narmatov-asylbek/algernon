from django.shortcuts import render
from django.views.generic import View

from chapters.models import Chapter
# Create your views here.


class ReadChaptersView(View):
    def get(self, request, book_id, chapter_id=None, *args, **kwargs):
        try:
            if chapter_id:
                chapter = Chapter.objects.get(book_id=book_id, id=chapter_id)
            else:
                chapter = Chapter.objects.get(book_id=book_id, id=1)
        except Chapter.DoesNotExist:
            chapter = "Chapter does not exist"
        context = {
            'chapter': chapter
        }
        return render(request, 'reader/read_chapter.html', context)