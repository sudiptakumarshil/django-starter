from django.urls import path
from .views import face_login

urlpatterns = [
    path("", face_login, name="face_login"),
]
