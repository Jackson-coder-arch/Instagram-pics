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



def newPost(request):
    
   

    return render(request,'home.html')




#  if request.method == 'POST':
#         form = request.FILES.getlist('content')
#         caption = form.cleaned_data.get('caption')

#         for files in files:
#             file_instance = PostFileContent(file=file, user=user)
#             file_instance.save()
#             files_objs.append(file_instance)

#         p,created = Post.objects.get_or_create(image_caption=image_caption, user = user)
#         p.save()
#         return redirect('home')

#     else:
        
#         form = NewPostForm()

#         context = {
#             'form' : form,
#         }