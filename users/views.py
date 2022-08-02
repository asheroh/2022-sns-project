# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect
from main.models import Post
from django.contrib.auth.models import User


def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    # 로그인한 유저이름과 글 작성자 이름이 동일한 글 필터링
    context = {
        'user' : user,
        'posts' : Post.objects.filter(writer=user)
    }
    return render(request, 'users/mypage.html', context)

def follow(request, id):
    user = request.user
    followed_user = get_object_or_404(User, pk=id)
    is_follower = user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', followed_user.id)