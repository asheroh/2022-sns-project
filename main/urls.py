from django.urls import path, include
from .views import *

urlpatterns = [
    path('', include('sns_project.urls')),
    path('writepage/', showwrite, name="showwrite"),
    path('historypage/', showhistory, name="showhistory"),
    path('photopage/', showphoto, name="showphoto"),
    path('characterpage/', showcharacter, name="showcharacter"),
    path('hobbypage/', showhobby, name="showhobby"),
]
