from django.contrib import admin
from .models import (
    Profile,
    Image_posts,
    Comment,
)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display =('user','name',)

@admin.register(Image_posts)
class Image_posts(admin.ModelAdmin):
    pass

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    pass


