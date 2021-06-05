from django.contrib import admin

from .models import Chapter

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    pass
