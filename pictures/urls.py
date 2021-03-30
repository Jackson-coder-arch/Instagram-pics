from django.urls import path,re_path

from . import views


urlpatterns = [
    path('',views.home, name = 'home'),
    path('NewPost/',views.NewPost, name ='NewPost'),
    # re_path(r'^Newpost/',newPost),
]