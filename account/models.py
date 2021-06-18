from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudentProfile(models.Model):
    BATCHES = tuple([('1st year 1st semester', '1st year 1st semester'), ('1st year 2nd semester', '1st year 2nd semester'),
                     ('2nd year 1st semester', '2nd year 1st semester'), ('2nd year 2nd semester', '2nd year 2nd semester'),('3rd year 1st semester', '3rd year 1st semester'), ('3rd year 2nd semester', '3rd year 2nd semester'),
                     ('4th year 1st semester', '4th year 1st semester'), ('4th year 2nd semester', '4th year 2nd semester')])
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic', default='img_avatar2.png')
    fname = models.CharField(max_length=50, blank=True)
    lname = models.CharField(max_length=50, blank=True)
    year_semester = models.CharField(max_length=50, choices=BATCHES, default="Select")
    batch = models.CharField(max_length=50)
    contantnum = models.CharField(max_length=15, blank=True, null=True)


    def __str__(self):
        return self.fname




class Teacher(models.Model):
    name = models.CharField(max_length=200, unique=True)
    dept = models.CharField(max_length=200, blank=True)
    teacherid = models.CharField(max_length=200, blank=True)
    mobilenum = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return str(self.name)
