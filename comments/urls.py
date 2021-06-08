from django.urls import path


from .views import post_comment

app_name = 'comments'
urlpatterns = [
    path('book/<int:id>/add-comment/', post_comment, name='post_comment')
]