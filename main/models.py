from enum import unique
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db import models
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your models here.


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    # created_at = models.DateField(auto_now_add=True)
    # updated_at = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="post/", blank=True, null=True)
    like_user_set = models.ManyToManyField(
        User, blank=True, related_name="likes_user_set", through="Like")
    dislike_user_set = models.ManyToManyField(
        User, blank=True, related_name="dislikes_user_set", through="Dislike")

    def _str_(self):
        return self.title

    def summary(self):
        return self.body[:20]

    @property
    def like_count(self):
        return self.like_user_set.count()

    @property
    def dislike_count(self):
        return self.dislike_user_set.count()


class Comment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)


class CommentUpdate(UpdateView):
    model = Comment
    fields = ['text']
    template_name_suffix = '_update'
    # success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '수정할 권한이 없습니다.')
            return HttpResponseRedirect('/')
            # 삭제 페이지에서 권한이 없다! 라고 띄우거나
            # detail페이지로 들어가서 삭제에 실패했습니다. 라고 띄우거나
        else:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)


class CommentDelete(DeleteView):
    model = Comment
    template_name_suffix = '_delete'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '삭제할 권한이 없습니다.')
            return HttpResponseRedirect('/')
        else:
            return super(CommentDelete, self).dispatch(request, *args, **kwargs)


# 좋아요 모델
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'post'))

# 싫어요 모델


class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'post'))
