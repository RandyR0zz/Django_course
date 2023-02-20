from email.policy import default
from django.shortcuts import render, redirect
from .models import Post, Author
from .forms import AddPost
import datetime
import re
from django.http import HttpRequest, HttpResponse


def home(request):
    return render(request, 'home.html')

def note(request):
    return render(request, 'note.html')

def about(request):
    return render(request, 'about_us.html')

def posts(request):
    all_posts = Post.objects.all().order_by('-issued')
    return render(request, 'posts.html', {'posts': all_posts})

def post(request, id):
    try:
        post = Post.objects.get(id=id)
    except:
        post = ""
    return render(request, 'post.html', {'post': post})

def add_post(request):
    
    if request.method == 'POST':
        new_form = AddPost(request.POST, request.FILES)

        if new_form.is_valid():
            post = Post()
            post.author = Author.objects.all()[0]
            post.issued = datetime.datetime.now()
            post.title = new_form.cleaned_data["title"]
            post.ingridients = new_form.cleaned_data["ingridients"]
            post.content = new_form.cleaned_data["content"]
            post.save()

            return redirect('note')

    else:
        new_form = AddPost()
    return render(request, 'add_post.html', {'new_form': new_form})
