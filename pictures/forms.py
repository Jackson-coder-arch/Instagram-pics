from django import forms
from .models import Image_posts

class Image_posts(forms.ModelForm):
    class Meta:
        model = Image_posts
        fields =('image','image_name','image_caption')

