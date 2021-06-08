import json
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.views.decorators.http import require_POST

from .forms import CommentForm
from .models import Comment
from books.models import Book


@login_required
@require_POST
def post_comment(request, id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        book = get_object_or_404(Book, id=id)
        author = request.user
        comment_text = json.load(request)['comment_text']
        comment = Comment.objects.create(book=book, user=author, comment_text=comment_text)
        return JsonResponse(comment.serialize(), status=200)
