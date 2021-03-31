from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Image_posts,Profile,Comment
from django.contrib.auth.forms import UserCreationForm
from .forms import ImageForm

# Create your views here.

def home(request):
    if request.method == 'GET':
        photos = Image_posts.get_images()


    return render(request,'home.html',{'photos':photos})



def NewPost(request):

    if request.method == 'POST':

        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            print('form is valid')
            post = form.save(commit=False)
            post.save()
            return redirect('home')

    else:
        form = ImageForm()
        
   
    return render(request,'newpost.html',{'form':form})


def register(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'django_registration/registration_form')


