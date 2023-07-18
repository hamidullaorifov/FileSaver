from django.shortcuts import render
from urllib.parse import quote,unquote
# Create your views here.
from rest_framework.views import APIView
from .models import File
from rest_framework.response import Response

class UploadFileView(APIView):

    def post(self,request):
        input_file = request.FILES.get('file')
        if input_file:
            file = File(file=input_file)
            file.save()
            file_url = request.build_absolute_uri(file.url)
            return Response({'file_url':file_url})
        return Response('Invalid data',status=400)