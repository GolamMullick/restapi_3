from django.db import models
from uuid import uuid4

def generateUUID():
    return str(uuid4())

class Student(models.Model):

    id = models.CharField(default=generateUUID, max_length=36, primary_key=True, editable=False)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    nationality=models.CharField(max_length=50)
    age=models.CharField(max_length=50)

class School(models.Model):
    name=models.CharField(max_length=20)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    maxstudent=models.IntegerField(default=10)
    location=models.CharField(max_length=50)
