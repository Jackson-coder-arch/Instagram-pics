from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
# from .forms import NewPostForm,
from .models import Image_posts,Profile,Comment

# Create your views here.
def home(request):
    images = Image_post.objects.all()
    current_user = request.user
    users = Profile.objects.all()

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FIlES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)

        else:
            form = NewPostForm()
            params ={
                images : images,
                'form': form,
                'users': users,
            }

        return render(request,'home.html', params)






def newPost(request):
    user = request.user
    files_objs = []

    if request.method == 'POST':
        form = request.FILES.getlist('content')
        caption = form.cleaned_data.get('caption')

        for files in files:
            file_instance = PostFileContent(file=file, user=user)
            file_instance.save()
            files_objs.append(file_instance)

        p,created = Post.objects.get_or_create(image_caption=image_caption, user = user)
        p.save()
        return redirect('home')

    else:
        
        form = NewPostForm()

        context = {
            'form' : form,
        }

    return render(request,'newpost.html',context)