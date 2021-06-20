from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Semester(models.Model):
    """docstring for Dept."""
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Dept(models.Model):
    """docstring for Dept."""
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Batch(models.Model):
    """docstring for Dept."""
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Semester(models.Model):
    """docstring for Dept."""
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name



class StudentProfile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic', default='img_avatar2.png')
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    year_semester = models.ForeignKey(Semester, default="", on_delete=models.CASCADE)
    contantnum = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic_teacher', default='teacher.jpeg')
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    teacherid = models.CharField(max_length=200, blank=True)
    mobilenum = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return str(self.teacherid)
