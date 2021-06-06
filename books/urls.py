from django.urls import path

from .views import (BookList, BookDetailView, AddBookView, UpdateBookTextView,
                    UpdateBookSettings, AddCycleView, DeleteCycleView, EditCycleView)
from .views import add_to_library, add_like_to_book

app_name = 'books'
urlpatterns = [
    path('book/<int:id>', BookDetailView.as_view(), name='detail'),
    path('book/<int:book_id>/library/', add_to_library, name='add_to_library'),
    path('book/<int:book_id>/like/', add_like_to_book, name='add_like_to_book'),
    path('books/<slug:slug>/', BookList.as_view(), name='book_list_by_genre'),
    path('', BookList.as_view(), name="homepage"),

    path('new/', AddBookView.as_view(), name='new_book'),
    path('work/<int:pk>/edit/', UpdateBookSettings.as_view(), name='update_book'),
    path('work/<int:id>/edit/content/', UpdateBookTextView.as_view(), name='update_book_content'),
    path('works/cycle/add', AddCycleView.as_view(), name='new_cycle'),
    path('u/works/series/<int:id>/delete/', DeleteCycleView.as_view(), name='delete_cycle'),
    path('works/series/<int:id>/edit/', EditCycleView.as_view(), name='edit_cycle'),
]
