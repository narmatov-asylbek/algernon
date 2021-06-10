from django.shortcuts import reverse
from django.db import models

from books.models import Book
from django.conf import settings
from django_quill.fields import QuillField


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='author_reviews'
    )
    content = QuillField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Review by %s to book %s on id %s" %(self.book.title, self.author.username, self.id )

    def get_absolute_url(self):
        return reverse('reviews:review_detail', args=[self.book.id, self.id])