from django.urls import path

from . import views

app_name = 'authors'
urlpatterns = [
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('works/', views.AuthorsCreatedBookList.as_view(), name='author_books'),
    path('works/series/', views.AuthorsCycleList.as_view(), name='authors_cycles'),
]