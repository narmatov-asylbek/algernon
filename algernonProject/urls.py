from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('', include('books.urls', namespace='books')),
    path('u/', include('authors.urls', namespace='authors')),
    path('reader/', include('reader.urls', namespace='reader')),
    path('', include('chapters.urls', namespace='chapters')),
    path('account/', include('account.urls', namespace='account')),
    path('comments/', include('comments.urls', namespace='comments')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)