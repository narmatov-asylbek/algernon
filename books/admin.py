from django.contrib import admin

from .models import Cycle, Genre, Type, Book, Library
# Register your models here.

admin.site.register(Cycle)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Type)
admin.site.register(Library)