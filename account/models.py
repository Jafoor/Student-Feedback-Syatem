from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from datetime import datetime
import hashlib

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


# class EmailConfirmation(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     activation_key = models.CharField(max_length=500)
#     email_confirmed = models.BooleanField(default=False)
#     date_created = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.user.email
#
#     class Meta:
#         verbose_name_plural = 'User Email-Confirmed'



class StudentProfile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic', default='img_avatar2.png')
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    year_semester = models.ForeignKey(Semester, default="", on_delete=models.CASCADE)
    contantnum = models.CharField(max_length=15, blank=True, null=True)
    pass_updated = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic_teacher', default='teacher.jpeg')
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    teacherid = models.CharField(max_length=200, blank=True)
    mobilenum = models.CharField(max_length=15, blank=True)
    pass_updated = models.BooleanField(default=False)

    def __str__(self):
        return str(self.teacherid)


# @receiver(post_save, sender=User)
# def create_user_email_confirmation(sender, instance, created, **kwargd):
#     if created:
#         dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         email_confirmed_instance = EmailConfirmation(user=instance)
#         user_encode = f'{instance.email}-{dt}'.encode()
#         activation_key = hashlib.sha224(user_encode).hexdigest()
#         email_confirmed_instance.activation_key = activation_key
#         email_confirmed_instance.save()
