from django.test import TestCase
from .models import(
    Image_posts,
    Profile,
    Comment,
    Follow,
    
)

class TestImage_posts(TestCase):
    def setUp(self):
        self.profile_test = Profile(name='jack', user=User(username='jack'))
        self.profile_test.save()

        self.image_posts_test =Image_posts(image_name='test',image_caption='default test',user=self.profile_test)

    def test_instance(self):
        sef.assertTrue(isinstance(self.image_posts_test,Image_posts))

    def test_save_image_post(self):
        self.image_posts_test.save_image_post()
        after = Image_posts.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image_posts(self):
        self.image_posts_test.delete_image_post()
        after = Profile.objects.all()
        self.assertTrue(len(after) < 1)
        

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='jack')
        self.user.save()

        self.profile_test = Profile(name='image',profile_photo='default.jpg',bio='its a profile test',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)

