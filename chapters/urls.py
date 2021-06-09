from django.urls import path

from .views import AddChapterView, UpdateChapterView, delete_chapter

app_name = 'chapters'
urlpatterns = [
    path('book/<int:book_id>/chapter/<int:id>/edit', UpdateChapterView.as_view(), name='edit_chapter'),
    path('book/<int:book_id>/chapter/<int:chapter_id>/delete', delete_chapter, name='delete_chapter'),
    path('book/<int:book_id>/add/chapter', AddChapterView.as_view(), name='add_chapter'),

]
