from django.urls import path,re_path

from .views import (
    home,
    newPost,
)


urlpatterns = [
    path('',home, name = 'home'),
    path('newPost/',newPost, name ='newPost'),
    re_path(r'^newpost/',newPost),
]