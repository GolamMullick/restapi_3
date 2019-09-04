from django.shortcuts import render
from rest_framework import viewsets
from .models import Student,School
from .serializers import StudentSerializer,SchoolSerializer
from django.shortcuts import render
from rest_framework import viewsets
from .models import Student,School
from .serializers import StudentSerializer,SchoolSerializer
from rest_framework.filters import SearchFilter,OrderingFilter

class StudentView(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=(SearchFilter,OrderingFilter)
    search_fields=('firstname','age')

class SchoolView(viewsets.ModelViewSet):
    queryset=School.objects.all()
    serializer_class=SchoolSerializer
    filter_backends=(SearchFilter,OrderingFilter)
    search_fields=('location','name')
