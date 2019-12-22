from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import Post
from .forms import PostCreateForm

def home(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')
    }
    return render(request, 'sharestory/home.html', context)

def liked_posts(request):
    posts = Post.objects.filter(likes=request.user).order_by('-date_posted')
    context = {
        'posts': posts
    }
    return render(request, 'sharestory/home.html', context)

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f"{title} post is successfully created!!!")
            return redirect('home')
    else:
        form = PostCreateForm()
    return render(request, 'sharestory/post_create.html', {'form': form})

def post_like(request):
    post = Post.objects.get(id=request.POST.get('post_id'))
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('home')
