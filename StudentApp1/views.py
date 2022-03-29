from email.policy import EmailPolicy
##from msilib.schema import ServiceInstall
from pyexpat import model
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import students
from . serializers import Studentserializer

class StudentList(APIView):
    def get(self, request):
        student1 = students.objects.all()
        serializer = Studentserializer(student1, many = True)
        return Response(serializer.data)

# Create your views here.
