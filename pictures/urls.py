from django.urls import path,re_path

from .views import (
    home,
    newPost,
)


urlpatterns = [
    path('',home, name = 'home'),
    re_path(r'^newpost/',newPost)
]