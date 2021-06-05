from django.urls import path

from . import views

app_name = 'reader'
urlpatterns = [
    path('<int:book_id>/', views.ReadChaptersView.as_view(), name='read_book'),
    path('<int:book_id>/chapter/<int:chapter_id>', views.ReadChaptersView.as_view(), name='read_chapter'),
]