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


def update_comment(request, comment_id, post_id):

    my_comment = Comment.objects.get(id=comment_id)
    comment_form = commentForm(instance=my_comment)
    if request.method == "POST":
        update_form = CommentForm(request.POST, instance=my_comment)
        if update_form.is_valid():
            update_form.save()
            return redirect('detail', post_id)
        return render(request, 'review_update.html', {'comment_form': comment_form})


def delete_comment(request, id):
    comment = get_object_or_404(Comment, pk=id)
    post_id = comment.post.id
    comment.delete()
    return redirect('post:detail', post_id)


def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('main:posts')


def posts(request):
    posts = Post.objects.all()
    return render(request, 'main/posts.html', {'posts': posts})


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


def dispatch(self, request, *args, **kwargs):
    object = self.get_object()
    if request.method == "POST":
        super().post(request, *args, **kwargs)
    else:
        super().post(request, *args, **kwargs)
