from django.urls import path
from .views import *
from .views import update_comment, delete_comment

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('writepage/', showwrite, name="showwrite"),
    path('historypage/', showhistory, name="showhistory"),
    path('photopage/', showphoto, name="showphoto"),
    path('characterpage/', showcharacter, name="showcharacter"),
    path('hobbypage/', showhobby, name="showhobby"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('<str:id>', detail, name="detail"),
    path('posts/', posts, name="posts"),
    path('new/', new, name="new"),
    path('<int:post_id>/create_comment', create_comment, name="create_comment"),
    path('<str:post_id>/<str:comment_id>/update_comment',
         update_comment, name="update_comment"),
    path('<str:post_id>/<str:comment_id>/edit_comment',
         edit_comment, name="edit_comment"),
    # comment UD 시에는 post와 comment id 둘 다 필요
    path('<str:comment_id>/delete_comment',
         delete_comment, name="delete_comment"),
]
