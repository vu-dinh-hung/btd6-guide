from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Category
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def slug(request, slug, path=''):
    # Category view, displays all posts
    categories = [c.category_slug for c in Category.objects.all()]
    if slug in categories:
        all_current_posts = Post.objects.filter(post_category__category_slug=slug)
        current_category = Category.objects.get(category_slug=slug)
        return render(request,
                      template_name='main/category-view.html',
                      context={'posts': all_current_posts,
                               'current_category': current_category})
    
    # Post view, displays post
    posts = [p.post_slug for p in Post.objects.all()]
    if slug in posts:
        current_post = Post.objects.get(post_slug = slug)
        return render(request,
                      template_name='main/post-view.html',
                      context={'p': current_post})
    
    return HttpResponse(f'{slug} does not exist (yet).')

def index(request):
    return render(request,
                  template_name='main/home.html',
                  context={'posts': Post.objects.all})

def guides(request):
    return render(request,
                  template_name='main/all-categories.html',
                  context={'categories': Category.objects.all})

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            messages.success(request, f'New account {username} created.')
            return redirect('/')
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}: {form.error_messages[msg]}')

    form = UserCreationForm
    return render(request,
                  template_name='main/register.html',
                  context={'form': form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Logged in as {username}.')
                return redirect('/')
            else:
                messages.error(request, f'Invalid username or password.')
        else:
            messages.error(request, f'Invalid username or password.')

    form = AuthenticationForm
    return render(request,
                  template_name='main/login.html',
                  context={'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('/')

def account_user(request):
    user = request.user
    return render(request,
                  template_name='main/account.html',
                  context={"user": user})