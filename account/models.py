from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


from pytils.translit import slugify
from django_quill.fields import QuillField


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    email = models.EmailField(_('Email'), unique=True)

    DS = "Don't Show"
    MALE = "Male"
    FEMALE = "Female"
    GENDER_CHOICES = (
        (DS, _("Don't Show")),
        (MALE, _("Male")),
        (FEMALE, _("Female"))
    )

    ONLY_MONTH_AND_DAY = "Only month and day"
    SHOW = "Show"
    BIRTHDAY_CHOICES = (
        (DS, _("Don't Show")),
        (ONLY_MONTH_AND_DAY, _("Only month and day")),
        (SHOW, _("Show birthday"))
    )
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='profile/%Y/%m-%d', default='images/no-image.png', blank=True)
    name = models.CharField(max_length=250, unique=True)
    status = models.CharField(max_length=250, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    birthday_visibility = models.CharField(max_length=40, choices=BIRTHDAY_CHOICES, default=DS)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default=DS)
    information = QuillField(max_length=1000, null=True, blank=True)

    friends = models.ManyToManyField("CustomUser", blank=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.slug:
            if not self.name:
                self.slug = slugify(self.username)
            self.slug = slugify(self.name)
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('account:profile', args=[self.slug])

    def get_account_lib_url(self):
        return reverse('account:library', args=[self.slug])

    def get_author_url(self):
        return reverse('authors:author_detail', args=[self.pk])

    def get_image_url(self):
        if not self.image:
            return None
        return self.image.url

    def get_subscribers(self):
        return Friend.objects.filter(to_user=self)

    def get_followings(self):
        return Friend.objects.filter(from_user=self)


class Contact(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='contact',
    )
    website = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    vk = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.email


class Friend(models.Model):
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='from_users'
    )
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='to_users'
    )

    def __str__(self):
        return "From %s to %s" % (self.from_user.name, self.to_user.name)
