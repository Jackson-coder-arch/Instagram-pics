from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# from django.utils import timezone

# Create your models here.
class Image_posts(models.Model):
    image = CloudinaryField('image')
    image_name =models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image_caption = models.TextField()
    # created_date = models.DateTimeField(default=timezone.now)
    # likes =models.ManyToManyField(User,related_name='likes')
    # user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='image_posts')

    class Meta:
        ordering = ["-pk"]

    def get_absolute_url(self):
        return f"/post/{self.id}"

    @property
    def get_all_comments(self):
        return self.comments.all()

    def save_image_post(self):
        self.save()

    def delete_image_post(self):
        self.delete()

    def __str__(self):
        return self.image_name




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=500,default='My Bio')
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)

    def __str__(self):
        return self.Profile

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

class Comment(models.Model):
    comment = models.TextField()
    # image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def __str__(self):
        return self.comment


class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'

# class Likes(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_like')
#     image = models.ForeignKey(Image_posts, on_delete=models.CASCADE,related_name='image_like')

class InstagramLetterRecipients(models.Model):
    name = models.CharField(max_length= 30)
    email =models.EmailField(max_length=30)
    # date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


