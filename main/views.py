from django.shortcuts import render , get_object_or_404, redirect
from .models import *
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.utils.timezone import utc
from django.contrib.auth.models import Group
from account.models import *

# Create your views here.

def listToString(s):

    str1 = ""
    l = len(s)
    i = 0
    for ele in s:
        if(i != l-1):
            str1 += ele
            str1 += ','
        else:
            str1 += ele
        i += 1

    return str1

def revpoint(l):

    str2 = ""
    i = 0
    for j in range(0,l):
        if j != l-1:
            str2 += '0'
            str2 += ','
        else:
            str2 += '0'
    return str2


@login_required(login_url = '/login/')
def addquestion(request):

    if request.method == 'POST':
        name = request.POST.get('question')
        typ1 = request.POST.get('type1')
        typ2 = request.POST.get('type2')
        typ3 = request.POST.get('type3')
        typ4 = request.POST.get('type4')
        typ5 = request.POST.get('type5')

        b = Question(name = name, typ1 = typ1, typ2 = typ2, typ3=typ3, typ4=typ4, typ5=typ5)
        b.save()
        messages.info(request, 'Successfully added to database')


    return render(request, 'back/addquestion.html')

@login_required(login_url = '/login/')
def allquestion(request):

    return render(request, 'back/allquestion.html')

@login_required(login_url = '/login/')
def addsubject(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        subcode = request.POST.get('subcode')

        b = Subject(name = name, dept = dept, subcode = subcode)
        b.save()
        messages.info(request, 'Successfully added to database')


    return render(request, 'back/addsubject.html')

@login_required(login_url = '/login/')
def addreviewset(request):

    sem = {1:'1st year 1st semester', 2:'1st year 2nd semester', 3:'2nd year 1st semester',4:'2nd year 2nd semester',5:'3rd year 1st semester',6:'3rd year 2nd semester',7:'4th year 1st semester',8:'4th year 2nd semester'}
    teachers = Teacher.objects.all().order_by('dept')

    subjects = Subject.objects.all().order_by('dept')
    print(teachers)

    if request.method == 'POST':
        name = request.POST.get('name')
        teacher = request.POST.get('teacher')
        subject = request.POST.get('subject')
        endtime = request.POST.get('endtime')
        semester = request.POST.get('semester')
        b = ReviewSet(name =name,teacher=teacher,subject=subject,endtime=endtime,semester=semester)
        print(name)
        print(teacher)
        print(semester)
        print(endtime)
        print(subject)
        b.save()
        return redirect('setquestion',pk=b.pk)

    return render(request, 'back/addreviewset.html',{'semester':sem,'teachers':teachers,'subjects':subjects})

@login_required(login_url = '/login/')
def setquestion(request,pk):

    question = Question.objects.all().order_by('-pk')

    if request.method == 'POST':

        p = request.POST.getlist('questions')
        pp = listToString(p)
        l = len(p)
        b = ReviewSet.objects.get(pk=pk)
        ll = revpoint(l)
        b.question = pp
        b.revpoint = ll
        print(ll)
        b.save()

    return render(request, 'back/setquestions.html',{'question':question})

@login_required(login_url = '/login/')
def submitanswer(request,pk):

    q = ReviewSet.objects.get(pk=pk)
    question = q.question.all()
    usr = request.user.username

    if request.method == 'POST':

        if usr not in q.given:
            total = q.totalpoint
            for i in question:
                value = request.POST.get(i.name)
                total += int(value)
            q.totalpoint = total
            given = q.given
            given += usr
            q.given = given
            avg = (total*100)/(len(question)*5)
            q.avg = avg
            q.save()
            messages.info(request, 'Successfully added review')
            return redirect('home')
        else:
            messages.info(request, 'You given it earlier')
            return redirect('home')


    return render(request, 'front/submitanswer.html',{'question':question})
