from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.


def showmain(request):
    posts = Post.objects.all()
    return render(request, 'main/show.html', {'blogs': posts})


def showwrite(request):
    return render(request, 'main/writepage.html')


def showhistory(request):
    return render(request, 'main/historypage.html')


def showphoto(request):
    return render(request, 'main/photopage.html')


def showcharacter(request):
    return render(request, 'main/characterpage.html')


def showhobby(request):
    return render(request, 'main/hobbypage.html')


def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'main/detail.html', {'post': post})


def new(request):
    return render(request, 'main/new.html')


def create(request):
    new_blog = Post()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']
    new_blog.save()
    return redirect('detail', new_blog.id)
