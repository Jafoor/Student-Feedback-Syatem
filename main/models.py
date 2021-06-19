from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils.timezone import now
from account.models import *
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=250, blank=False)
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
        return str(self.subject.name)


class Question(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return str(self.name)

class ReviewSet(models.Model):
    name = models.CharField(max_length=200, blank=True)
    semester = models.ForeignKey(Semester, default="", on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, default="", on_delete=models.CASCADE)
    dept = models.ForeignKey(Dept, default="", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, default="", on_delete=models.CASCADE)
    question = models.ManyToManyField(Question)
    created = models.DateTimeField(default=datetime.now)
    endtime = models.DateTimeField( blank=True,null=True)
    stop = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Review(models.Model):
    reviewfor = models.ForeignKey(ReviewSet, default="", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default="", on_delete=models.CASCADE)
    point = models.IntegerField(default=0)

    def __str__(self):
        return (self.question.name)


class ReviewDetails(models.Model):

    review = models.OneToOneField(ReviewSet, on_delete=models.CASCADE)
    usergiven = models.IntegerField(default=0)
    totalpoint = models.DecimalField(max_digits=20, decimal_places=4, default=0.0)
    avg = models.DecimalField(max_digits=20, decimal_places=4, default=0.0)

    def __str__(self):
        return str(self.review.name)


@receiver(post_save, sender=ReviewSet)
def reviewdetails_created(sender, instance, created, **kwargd):
    if created:
        reviewdetails = ReviewDetails(review=instance)
        reviewdetails.save()
