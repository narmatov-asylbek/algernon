from .models import Genre


def genre_list(request):
    return {
        'genres': Genre.objects.all()
    }