from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http.response import JsonResponse

# Create your views here.
from django.views.generic import ListView, UpdateView
from django.views.generic import View
from books.models import Book, Cycle
from books.forms import BookForm, CycleForm


class AuthorsBookList(LoginRequiredMixin, ListView):
    template_name = 'authors/created_books.html'
    model = Book
    context_object_name = 'books'

    def get_queryset(self, *args, **kwargs):
        author = self.request.user
        return Book.objects.filter(author=author)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.request.user
        return context



class AuthorsCycleList(ListView):
    model = Cycle
    template_name = 'authors/books/created_cycles.html'
    context_object_name = 'cycles'

    def get_queryset(self):
        queryset = Cycle.objects.filter(creator=self.request.user)
        return queryset


