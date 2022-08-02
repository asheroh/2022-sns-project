# Create your views here.
from django.shortcuts import get_object_or_404, render
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
