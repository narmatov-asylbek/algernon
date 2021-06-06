from django.urls import path

from .views import AddChapterView, UpdateChapterView

app_name = 'chapters'
urlpatterns = [
    path('book/<int:book_id>/add/chapter', AddChapterView.as_view(), name='add_chapter'),
    path('book/<int:pk>/edit/chapter', UpdateChapterView.as_view(), name='edit_chapter'),
]
