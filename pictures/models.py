from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Image_posts(models.Model):
    image = CloudinaryField('image')
    image_name =models.ForeignKey('Profile',on_delete=models.CASCADE,null=True,related_name='image_posts')
    image_caption = models.TextField()
    location = models.CharField(max_length=60)


    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images


    class Meta:
        ordering = ["-pk"]

    # def get_absolute_url(self):
    #     return f"/post/{self.id}"

    @property
    def get_all_comments(self):
        return self.comments.all()

    def save_image_post(self):
        self.save()

    def delete_image_post(self):
        self.delete()

    def __str__(self):
        return self.image_caption




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=500,default='My Bio')
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

class Comment(models.Model):
    comment = models.TextField()
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






