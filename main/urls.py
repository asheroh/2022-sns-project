from django.urls import path
from .views import *
from .views import update_comment, delete_comment
# from . import views

app_name = "main"
urlpatterns = [
     path('', showmain, name="showmain"),
     path('writepage/', showwrite, name="showwrite"),
     path('photopage/', showphoto, name="showphoto"),
     path('mbti/', showmbti, name="showmbti"),
     path('edit/<int:id>', edit, name="edit"),
     path('update/<int:id>', update, name="update"),
     path('delete/<int:id>', delete, name="delete"),
     path('<str:id>', detail, name="detail"),
     path('posts/', posts, name="posts"),
     path('new/', new, name="new"),
     path('<int:post_id>/create_comment', create_comment, name="create_comment"),
     path('<str:post_id>/<str:comment_id>/update_comment', update_comment, name="update_comment"),
     path('<str:post_id>/<str:comment_id>/edit_comment', edit_comment, name="edit_comment"),

     # comment UD 시에는 post와 comment id 둘 다 필요
     path('<str:comment_id>/delete_comment',
          delete_comment, name="delete_comment"),

     # like, dislike toggle
     path('like_toggle/<int:post_id>/', like_toggle, name="like_toggle"),
     path('dislike_toggle/<int:post_id>/',
          dislike_toggle, name="dislike_toggle"),

     # 좋아요 목록
     path('my_like/<int:user_id>/', my_like, name="my_like"),
]
