from django import forms
from .models import Image_posts

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image_posts
        fields =('image','image_caption')

