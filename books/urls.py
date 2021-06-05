from django.urls import path

from .views import (BookList, BookDetailView, AddBookView, UpdateBookTextView,
                    UpdateBookSettings, AddCycleView, DeleteCycleView, EditCycleView)

app_name = 'books'
urlpatterns = [
    path('book/<int:id>', BookDetailView.as_view(), name='detail'),
    path('books/<slug:slug>/', BookList.as_view(), name='book_list_by_genre'),
    path('', BookList.as_view(), name="homepage"),

    path('new/', AddBookView.as_view(), name='new_book'),
    path('work/<int:pk>/edit/', UpdateBookSettings.as_view(), name='update_book'),
    path('work/<int:id>/edit/content/', UpdateBookTextView.as_view(), name='update_book_content'),
    path('works/cycle/add', AddCycleView.as_view(), name='new_cycle'),
    path('u/works/series/<int:id>/delete/', DeleteCycleView.as_view(), name='delete_cycle'),
    path('works/series/<int:id>/edit/', EditCycleView.as_view(), name='edit_cycle'),
]
