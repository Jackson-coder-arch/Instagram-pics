from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Image_posts,Profile,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ImageForm

# Create your views here.

def home(request):
    if request.method == 'GET':
        photos = Image_posts.get_images()


    return render(request,'home.html',{'photos':photos})


@login_required(login_url='/accounts/login/')
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
    if request.method =='POST':
        form = UserCreationForm()
        context = {'form':form}
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'django_registration/registration_form',{'form':form} )


@login_required(login_url='/accounts/login/')
def profile(request):
    if request.method == 'POST':
        form = Profile(request.POST, request.FILES)
        if form.is_valid():
            form = profile.save(commit=False)
            form.save()
            return redirect('home')
    else:
        form = Profile()

    return render(request,'profile.html',{'form':form})







