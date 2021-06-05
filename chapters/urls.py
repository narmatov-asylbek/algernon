from django.urls import path

from .views import AddChapterView

app_name = 'chapters'
urlpatterns = [
    path('book/<int:book_id>/add/chapter', AddChapterView.as_view(), name='add_chapter'),
]
