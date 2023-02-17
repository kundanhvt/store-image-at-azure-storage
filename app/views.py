from django.shortcuts import render, redirect
# from django.core.files.storage import default_storage
from django.conf import settings
from .models import Profile
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status


@api_view(['GET','POST'])
def upload_image(request):
    if request.method == 'POST':
        image = request.data.get('image',None)
        if image:
            # path = default_storage.save(image.name, image)
            # url = default_storage.url(path)
            res = Profile.objects.create(image=image)
            return JsonResponse({"image":res.image.url}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"message":"went wrong!!"}, status= status.HTTP_400_BAD_REQUEST)

