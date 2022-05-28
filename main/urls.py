from django.urls import path
from .views import *

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
    path('<str:post_id>/create_comment', create_comment, name="create_comment"),
]
