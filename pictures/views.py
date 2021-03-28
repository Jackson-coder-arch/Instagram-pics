from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
    # images = Image_post.objects.all()
    # current_user = request.user
    # users = Profile.objects.all()




def image_posts(request):

    return render(request,'image_posts')