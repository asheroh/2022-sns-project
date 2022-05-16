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
]
