from django.shortcuts import render, get_object_or_404
from .models import Album, Photo


def index(request):
    albums = Album.objects.all()
    return render(request, "index.html", {"albums":albums})


def album_view(request, album_pk):
    album = get_object_or_404(Album, pk=album_pk)
    photos = Photo.objects.filter(album=album)
    return render(request, "album.html", {"album":album, "photos":photos})


def photo_view(request, photo_pk):
    photo = get_object_or_404(Photo, pk=photo_pk)
    return render(request, "photo.html", {"photo":photo})
