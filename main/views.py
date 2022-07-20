from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.utils import timezone


# Create your views here.


def showmain(request):
    posts = Post.objects.all()
    return render(request, 'main/show.html', {'posts': posts})


def showwrite(request):
    return render(request, 'main/writepage.html')


def showphoto(request):
    return render(request, 'main/photopage.html')


def showmbti(request):
    return render(request, 'main/mbti.html')


def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'main/detail.html', {'post': post, 'comments': all_comments})


def new(request):
    return render(request, 'main/new.html')


def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('detail', new_post.id)


def create_comment(request, post_id):
    new_comment = Comment()
    new_comment.writer = request.user
    new_comment.content = request.POST['content']
    new_comment.post = get_object_or_404(Post, pk=post_id)
    new_comment.save()
    return redirect('main:detail', post_id)


def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'main/edit.html', {'post': edit_post})


def update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.image = request.FILES.get('image')
    update_post.save()
    return redirect('detail', update_post.id)


# 실패 코드
# def update_comment(request, comment_id, post_id):

#     my_comment = Comment.objects.get(id=comment_id)
#     comment_form = commentForm(instance=my_comment)
#     if request.method == "POST":
#         update_form = CommentForm(request.POST, instance=my_comment)
#         if update_form.is_valid():
#             update_form.save()
#             return redirect('detail', post_id)
#         return render(request, 'review_update.html', {'comment_form': comment_form})

def edit_comment(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comment = Comment.objects.get(id=comment_id)
    return render(request, 'main/edit_comment.html', {'post': post, 'comment': comment})


def update_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        comment.content = request.POST['content']
        comment.save()
        return redirect('main:detail', comment.post.id)
    return render(request, 'main:detail', {'comment': comment})


# 실패 코드
# def delete_comment(request, id):
#     comment = get_object_or_404(Comment, pk=id)
#     post_id = comment.post.id
#     comment.delete()
#     return redirect('post:detail', post_id)


def delete_comment(request, comment_id):
    delete_comment = Comment.objects.get(pk=comment_id)
    delete_comment.delete()
    return redirect('main:posts')
# 댓글 삭제 시에는 post id값 받아올 필요 없이 comment id값만 받아와도 충분


def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('main:posts')


def posts(request):
    posts = Post.objects.all()
    return render(request, 'main/posts.html', {'posts': posts})
