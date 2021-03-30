from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Image_posts,Profile,Comment
from .forms import Image_posts

# Create your views here.

def home(request):
    if request.method == 'GET':
        photos = Image_posts.objects.all()



    if request.method == 'POST':
        form = Image_postsForm(request.POST)
        if form.is_valid():
            print('form is valid')
    else:
        form = Image_postsForm()

    

    return render(request,'home.html',{'form': form ,'photos':photos})



def NewPost(request):
    
   

    return render(request,'home.html')



