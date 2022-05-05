from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.


def showmain(request):
    blogs = Post.objects.all()
    return render(request, 'main/show.html', {'blogs': blogs})


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
    return render(request, 'main/detail.html', {'blog': post})


def new(request):
    return render(request, 'main/new.html')


def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.save()
    return redirect('detail', new_post.id)
