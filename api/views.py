from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Resume
from .serializers import ResumeSerializer



class ResumeAPIView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    
    parser_classes = [MultiPartParser, FormParser]  # ✅ Important for file upload


    def get(self, request, pk=None):  # 'pk' is optional
        if pk is not None:
            # Return single record
            resume = get_object_or_404(Resume, pk=pk)
            serializer = ResumeSerializer(resume)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            #  Return all records
            resumes = Resume.objects.all()
            serializer = ResumeSerializer(resumes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response("get metthod")
    
    def post(self,request):
        
        serializer=ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("wow ! your resume is looking very good you just need to update it for every applications" \
            "and keep updating... ",status=200)
        else:
            return Response(serializer.errors, status=400)