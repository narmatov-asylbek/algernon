from django.shortcuts import render, reverse, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from books.models import Book
from .models import Review
from .forms import ReviewForm


@login_required
def create_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.author = request.user
            review.save()
            return HttpResponseRedirect(reverse('reviews:review_detail', args=[book.id, review.id]))
        return render(request, 'reviews/review_form.html', {'form': form, 'book':book})
    else:
        form = ReviewForm()
        context = {
            'form': form,
            'book': book
        }
        return render(request, 'reviews/review_form.html', context)


def review_list(request, book_id):
    if request.method == 'GET':
        book = get_object_or_404(Book, id=book_id)
        reviews = get_list_or_404(Review, book=book)
        context = {
            'book': book,
            'reviews': reviews
        }
        return render(request, 'reviews/review_list.html', context)


def review_detail(request, book_id, review_id):
    if request.method == 'GET':
        book = get_object_or_404(Book, id=book_id)
        review = get_object_or_404(Review, book=book, id=review_id)
        context = {
            'review': review,
            'book': book
        }
        return render(request, 'reviews/review_detail.html', context)


@login_required
def account_review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review, author=request.user)
        context = {
            'reviews': reviews
        }
        return render(request, 'reviews/account_review_list.html', context)