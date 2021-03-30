from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Image_posts,Profile,Comment
from .forms import InstagramLetterForm

# Create your views here.

def home(request):
    if request.method == 'GET':
        photos = Image_posts.objects.all()



    if request.method == 'POST':
        form = InstagramLetterForm(request.POST)
        if form.is_valid():
            print('form is valid')
    else:
        form = InstagramLetterForm()

    

    return render(request,'home.html',{'form': form ,'photos':photos})



def profile(request):
    
   

    return render(request,'profile.html')

def NewPost(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = InstagramLetterRecipient(name=name, email =email)
            recipient.save()
            HttpResponseRedirect('newpost')
    else:
        form = InstagramLetterForm()

    return render(request,'newpost.html',{'letterForm':form} )




