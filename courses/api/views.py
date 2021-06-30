import django.shortcuts
from rest_framework import generics
from ..models import Subject,Course 
from .serializers import SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class CourseEnrollView(APIView):
    def post(self,request,pk,format=None):
        course = get_object_or_404(Course,pk=pk)
        course.students.add(request.user)
        return Response({'enrolled':True})
