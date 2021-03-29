from django.shortcuts import render

# Create your views here.
def Image_posts(request):
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






def image_posts(request):

    return render(request,'image_posts')