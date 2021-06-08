from django.db import models

from django.conf import settings
from books.models import Book


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )
    comment_text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def serialize(self):
        return {
            'author': self.user.name,
            'author_image': self.user.get_image_url(),
            'comment_text': self.comment_text,
            'created_at': self.created_at
        }