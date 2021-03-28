from django.urls import path,re_path

from .views import (
    home,
    image_posts,
)


urlpatterns = [
    path('',home, name = 'home'),
    re_path(r'^image_posts/',image_posts)
]