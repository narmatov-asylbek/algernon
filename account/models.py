from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from pytils.translit import slugify
from django_quill.fields import QuillField


class CustomUserManager(BaseUserManager):
    def create_user(self, email, pseudonym, password, **extra_fields):
        if not email:
            raise ValueError(_('Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, pseudonym=pseudonym, **extra_fields)
        user.set_password(password)
        user.save()
        contact = Contact.objects.create(user=user)
        return user

    def create_superuser(self, email, pseudonym, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Must be set is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Must be set is_superuser=True'))

        return self.create_user(email, pseudonym, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
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
    pseudonym = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='profile/%Y/%m-%d', null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=250, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    birthday_visibility = models.CharField(max_length=40, choices=BIRTHDAY_CHOICES, default=DS)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default=DS)
    information = QuillField(max_length=1000, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['pseudonym']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.pseudonym)
        super().save(*args, **kwargs)


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


