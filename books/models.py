from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.conf import settings

from django_quill.fields import QuillField
from pytils.translit import slugify



class Cycle(models.Model):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('Book Cycle Creator')
    )
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name=_("Book Cycle Name")
    )
    desciption = models.TextField(max_length=1000, null=True, blank=True)
    is_finished = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']
        verbose_name = _("Book Cycle")

    def __str__(self):
        return self.name


class Type(models.Model):
    title = models.CharField(
        max_length=250,
        unique=True,
        verbose_name=_("Book Type")
    )

    class Meta:
        ordering = ['title']
        verbose_name = _("Book type")

    def __str__(self):
        return self.title


class Genre(models.Model):
    slug = models.SlugField()
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name=_("Book Genre Name")
    )
    is_important = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']
        verbose_name = _("Genre")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Book(models.Model):

    BOOK_CHOICES = (
        ("A", _("All")),
        ("O", _("Only friends")),
        ("N", _("Nobody"))
    )

    STATUS_CHOICES = (
        ("F", _("Finished")),
        ("D", _("Draft")),
        ("N", _("Not finished"))
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="books",
        verbose_name=_("Author")
    )
    cover = models.ImageField(upload_to="images/%Y-%m-%d/")
    title = models.CharField(max_length=150, unique=True, verbose_name=_("Book Name"))
    type = models.ForeignKey(
        Type,
        on_delete=models.SET_NULL,
        null=True,
        related_name="books",
        verbose_name=_("Book Type")
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books",
        verbose_name=_("Genre of the book")
    )
    cycle = models.ForeignKey(
        Cycle,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="books",
        verbose_name=_("Book Cycle")
    )
    description = models.TextField(max_length=1000, null=True, blank=True)
    remark = models.TextField(max_length=1000, null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="N")

    is_introductory = models.BooleanField(default=False)
    is_eighteen_plus = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    can_comment = models.CharField(max_length=2, choices=BOOK_CHOICES, default="N")
    can_read = models.CharField(max_length=2, choices=BOOK_CHOICES, default="N")
    can_download = models.CharField(max_length=2, choices=BOOK_CHOICES, default="N")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Book Info")
        verbose_name_plural = _("Books Info")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:detail', args=[self.id])

    def get_first_chapter(self):
        return reverse('reader:read_book', args=[self.id])

    def get_total_len(self):
        chapters = self.chapters.all()
        return sum([chapter.get_chapter_len() for chapter in chapters])

    def get_total_author_list_len(self):
        chapters = self.chapters.all()
        return round(sum([chapter.get_chapter_author_list_len() for chapter in chapters]), 2)

    def get_comment_count(self):
        return len([comment for comment in self.comments.all()])
    def get_can_download_options(self):
        if self.can_download == "A":
            return "Разрешено"
        elif self.can_download == "O":
            return "Разрешено только друзьям"
        else:
            return "Запрещено"



