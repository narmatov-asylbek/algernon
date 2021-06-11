from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import ListView, DetailView
from books.models import Book, Cycle
from django.contrib.auth.views import get_user_model


class AuthorsCreatedBookList(LoginRequiredMixin, ListView):
    """ View for showing user's created books """
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


class AuthorsCycleList(LoginRequiredMixin, ListView):
    """ View for showing list of user's cycles """
    model = Cycle
    template_name = 'books/created_cycles.html'
    context_object_name = 'cycles'

    def get_queryset(self):
        queryset = Cycle.objects.filter(creator=self.request.user)
        return queryset


class AuthorDetailView(DetailView):
    """ View for showing actual information about author"""
    model = get_user_model()
    template_name = 'authors/detail.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['books'] = Book.objects.filter(author_id=kwargs.get('id'))
        return context
