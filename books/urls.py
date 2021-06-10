from django.urls import path

from .views import (ShowCaseBookList, BookDetailView, AddBookView, UpdateBookTextView,
                    UpdateBookSettings, AddCycleView, EditCycleView, BookListView,
                    DeleteCycleView, CycleDetailView, BookListByGenreView)
from .views import add_to_library, add_like_to_book, delete_cycle

app_name = 'books'
urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:id>', BookDetailView.as_view(), name='detail'),
    path('book/<int:book_id>/delete', DeleteCycleView.as_view(), name='delete_book'),
    path('book/<int:book_id>/library/', add_to_library, name='add_to_library'),
    path('book/<int:book_id>/like/', add_like_to_book, name='add_like_to_book'),
    path('', ShowCaseBookList.as_view(), name="homepage"),

    path('work/genre/<slug:slug>/', BookListByGenreView.as_view(), name='books_by_genre'),
    path('work/series/<int:pk>', CycleDetailView.as_view(), name='cycle_detail'),
    path('new/', AddBookView.as_view(), name='new_book'),
    path('work/<int:pk>/edit/', UpdateBookSettings.as_view(), name='update_book'),
    path('work/<int:id>/edit/content/', UpdateBookTextView.as_view(), name='update_book_content'),
    path('works/cycle/add', AddCycleView.as_view(), name='new_cycle'),
    path('u/works/series/<int:id>/delete/', delete_cycle, name='delete_cycle'),
    path('works/series/<int:id>/edit/', EditCycleView.as_view(), name='edit_cycle'),
]
