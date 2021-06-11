from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _

from django_quill.fields import QuillField
from books.models import Book


class Chapter(models.Model):
    """ Model for book chapters. One book can have many chapters """
    STATUS = (
        ('D', _('Draft')),
        ('P', _('Published'))
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='chapters',
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='chapters'
    )
    title = models.CharField(max_length=200)
    text = QuillField(max_length=200000)
    status = models.CharField(max_length=2, choices=STATUS, default='D', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("Chapter")
        verbose_name_plural = _("Chapters")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('reader:read_chapter', args=[self.book.id, self.id])

    def get_chapter_len(self):
        return len(self.text.html)

    def get_chapter_author_list_len(self):
        if self.get_chapter_len() == 0:
            return 0
        else:
            return float(self.get_chapter_len() / 40000)

    def get_chapter_status(self):
        if self.status == 'D':
            return 'Не опубликовано'
        return 'Опубликовано'

    def get_chapter_update_url(self):
        return reverse('chapters:edit_chapter', args=[self.book.id, self.id])

    def get_chapter_delete_url(self):
        return reverse('chapters:delete_chapter', args=[self.book.id, self.id])
