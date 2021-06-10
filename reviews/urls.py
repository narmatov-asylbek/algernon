from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
    path('my-reviews/', views.account_review_list, name='account_reviews'),
    path('mt-reviews/<int:id>/delete/', views.delete_review, name='delete_review'),
    path('work/<int:book_id>/review/add', views.create_review, name='new_review'),
    path('work/<int:book_id>/reviews', views.review_list, name='review_list'),
    path('work/<int:book_id>/review/<int:review_id>', views.review_detail, name='review_detail'),
]