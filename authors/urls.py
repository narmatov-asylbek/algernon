from django.urls import path

from . import views

app_name = 'authors'
urlpatterns = [
    path('works/', views.AuthorsBookList.as_view(), name='author_books'),
    path('works/series/', views.AuthorsCycleList.as_view(), name='authors_cycles'),
]