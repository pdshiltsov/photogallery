from django.urls import path
from .views import album_view, index, photo_view

urlpatterns = [
    path('', index),
    path('album/<album_pk>', album_view),
    path('photo/<photo_pk>', photo_view),
]