from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path('<int:id>/mypage/', mypage, name="mypage"),
    # follow url추가
    path('<int:id>/follow', follow, name="follow"),
]
