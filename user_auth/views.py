from django.shortcuts import render, redirect
from django.contrib.auth import login
from utils.image_helper import ImageHelper
from django.contrib.auth.models import User


def face_login(request):
    if request.method == "POST":
        user = User.objects.get(username=request.POST["username"])
        user_face = user.profile.image
        input_image = request.FILES["input_image"]

        if ImageHelper.face_detector_helper(user_face.path, input_image):
            # login(request, user)
            # return redirect('dashboard')
            return render(request, "auth/face_login.html", {"error": "Face matched"})
        else:
            return render(
                request, "auth/face_login.html", {"error": "Face not matched"}
            )

    return render(request, "auth/face_login.html")
