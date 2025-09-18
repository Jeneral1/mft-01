from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Post
from .forms import PostForm

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        exclusive_posts = Post.objects.filter(user_id=request.user)
        other_posts = Post.objects.exclude(user_id=request.user)
    else:
        exclusive_posts = Post.objects.none()
        other_posts = Post.objects.all()
    return render(request, 'move/index.html', {
        'exclusive_posts': exclusive_posts,
        'other_posts': other_posts,
    })
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Bloghome')
    else:
        form = UserCreationForm()
    return render(request, 'move/signup.html',{'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            post.save()
            return redirect('Bloghome')
    else:
        form = PostForm()
    return render(request, 'move/create_post.html', {'form': form})