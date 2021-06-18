from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils.timezone import now
from account.models import *

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=250,)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    subcode = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['subcode']

    def __str__(self):
        return self.name


class SemesterSubject(models.Model):

    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject.name


class Question(models.Model):
    name = models.CharField(max_length=200, unique=True)
    typ1 = models.CharField(max_length=20, blank=True)
    typ2 = models.CharField(max_length=20, blank=True)
    typ3 = models.CharField(max_length=20, blank=True)
    typ4 = models.CharField(max_length=20, blank=True)
    typ5 = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

class ReviewSet(models.Model):
    name = models.CharField(max_length=200, blank=True)
    BATCHES = tuple([('1st year 1st semester', '1st year 1st semester'), ('1st year 2nd semester', '1st year 2nd semester'),
                     ('2nd year 1st semester', '2nd year 1st semester'), ('2nd year 2nd semester', '2nd year 2nd semester'),('3rd year 1st semester', '3rd year 1st semester'), ('3rd year 2nd semester', '3rd year 2nd semester'),
                     ('4th year 1st semester', '4th year 1st semester'), ('4th year 2nd semester', '4th year 2nd semester')])
    semester = models.CharField(max_length=50, choices=BATCHES, default="1st year 1st semester")
    teacher = models.ForeignKey(Teacher,
    on_delete=models.SET_NULL,
    null=True)
    subject = models.ForeignKey(Subject,
    on_delete=models.SET_NULL,
    null=True)
    question = models.ManyToManyField(Question)
    created = models.DateTimeField(default=datetime.now, blank=True)
    endtime = models.DateTimeField( blank=True,null=True)
    revpoint = models.CharField(max_length=1000, blank=True)
    given = models.TextField(blank=True)
    totalpoint = models.IntegerField(default=0)
    avg = models.IntegerField(default=0, blank=True, null=True)
    def __str__(self):
        return self.name


class Review(models.Model):

    semester = models.CharField(max_length=200, blank=True)
    teacher = models.CharField(max_length=200, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    point = models.IntegerField(default=100)
    session = models.CharField(max_length=50)
    question = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.semester
