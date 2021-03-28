from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.CharField()
    image_name =models.TextField()
    image_caption
    likes
    comments
    profile.Foreign_key

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_photo = models.ImageField(upload_to='images/',default='default.jpg')
    bio = models.TextField(max_length=500,default='My Bio')
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()
