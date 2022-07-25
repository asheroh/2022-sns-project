from email import message
import re
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Like, Dislike, User
from django.utils import timezone

# 좋아요 구현
from django.contrib.auth.decorators import login_required
# 2. 사용할 모듈 불러오기
# 2-1 POST 형식의 HTTP 통신만 받기
from django.views.decorators.http import require_POST
# 2-2 response를 변환하는 가장 가본 함수, html 파일, 이미지 등 다양한 응답
from django.http import HttpResponse
# 2-3 딕셔너리를 json 형식으로 바꾸기 위해
import json


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


@login_required
def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'main/detail.html', {'post': post, 'comments': all_comments})


def new(request):
    return render(request, 'main/new.html')


@login_required
def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('detail', new_post.id)


@login_required
def create_comment(request, post_id):
    new_comment = Comment()
    new_comment.writer = request.user
    new_comment.content = request.POST['content']
    new_comment.post = get_object_or_404(Post, pk=post_id)
    new_comment.save()
    return redirect('main:detail', post_id)


@login_required
def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'main/edit.html', {'post': edit_post})


@login_required
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

@login_required
def edit_comment(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comment = Comment.objects.get(id=comment_id)
    return render(request, 'main/edit_comment.html', {'post': post, 'comment': comment})


@login_required
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


@login_required
def delete_comment(request, comment_id):
    delete_comment = Comment.objects.get(pk=comment_id)
    delete_comment.delete()
    return redirect('main:detail', delete_comment.post.id)
# 댓글 삭제 시에는 post id값 받아올 필요 없이 comment id값만 받아와도 충분


@login_required
def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('main:posts')


@login_required
def posts(request):
    posts = Post.objects.all()
    return render(request, 'main/posts.html', {'posts': posts})


# like_toggle 함수
@require_POST               # POST 형식의 HTTP 통신,
@login_required             # 사용자가 login 한 상태라면
def like_toggle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_like, post_like_created = Like.objects.get_or_create(
        user=request.user, post=post)

    if not post_like_created:
        post_like.delete()
        result = "like_cancel"
    else:
        result = "like"
    context = {
        "like_count": post.like_count,
        "result": result
    }
    return HttpResponse(json.dumps(context), content_type="application/json")


# dislike_toggle 함수
@require_POST
@login_required
def dislike_toggle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_dislike, post_dislike_created = Dislike.objects.get_or_create(
        user=request.user, post=post)

    if not post_dislike_created:
        post_dislike.delete()
        result = "dislike_cancel"
    else:
        result = "dislike"
    context = {
        "dislike_count": post.dislike_count,
        "result": result
    }
    return HttpResponse(json.dumps(context), content_type="application/json")


@login_required
# 4. my_like 함수 작성하기
def my_like(request, user_id):
    user = User.objects.get(id=user_id)
    like_list = Like.objects.filter(user=user)
    context = {
        'like_list': like_list,
    }
    return render(request, 'main/my_like.html', context)
