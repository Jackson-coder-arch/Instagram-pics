from django.urls import path,re_path

from .views import (
    home,
    NewPost,
)


urlpatterns = [
    path('',home, name = 'home'),
    path('NewPost/',NewPost, name ='NewPost'),
    # re_path(r'^Newpost/',newPost),
]