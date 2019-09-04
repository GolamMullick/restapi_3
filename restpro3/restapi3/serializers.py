from rest_framework import serializers
from .models import Student
from .models import School


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('id','firstname','lastname','nationality','age')


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields=('name','student','maxstudent','location')
