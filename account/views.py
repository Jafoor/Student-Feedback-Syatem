from django.shortcuts import render , get_object_or_404, redirect
from .models import *
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from datetime import datetime
from django.utils.timezone import utc
from django.contrib.auth.models import Group, User
from main.models import *
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url = '/login/')
def home(request):
    user = request.user
    students = StudentProfile.objects.filter(user=user)
    teachers = Teacher.objects.filter(user=user)
    if students:
        student = get_object_or_404(StudentProfile, user=user)
        subjects = SemesterSubject.objects.filter(semester=student.year_semester)
        reviews = ReviewSet.objects.filter(semester = student.year_semester, dept=student.dept)
        list = []
        for rev in reviews:
            now = datetime.utcnow().replace(tzinfo=utc)
            given = Review.objects.filter(reviewfor=rev, user=user)
            if given:
                list.append('Given')
            elif rev.endtime < now:
                list.append('Time Over')
            else:
                list.append('Not Given')
        reviewslist = zip(reviews, list)
        context = {
            'stuprofile' : student,
            'user' : user,
            'subjects' : subjects,
            'reviewslist' : reviewslist,
        }
        return render(request, 'studentdashboard.html', context)
    elif teachers:
        teacher = get_object_or_404(Teacher, user=user)
        reviews = ReviewSet.objects.filter(teacher=teacher)
        list = []
        for rev in reviews:
            revdetais = ReviewDetails.objects.get(review=rev)
            list.append(revdetais)
        reviewslist = zip(reviews, list)

        context = {
            'teacher': teacher,
            'user': user,
            'reviewslist': reviewslist,
        }
        return render(request, 'teacherdashboard.html', context)
    elif user.is_staff:
        return render(request, 'admindashboard.html')
    else:
        return render(request, 'usernotgivenrole.html')







# def registerPage(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         form = CreateUserForm()
#
#         if request.method == 'POST':
#             form = CreateUserForm(request.POST)
#             if form.is_valid():
#                 user = form.save()
#                 username = form.cleaned_data.get('username')
#
#                 messages.success(request, 'Account was created for ' + username)
#                 print(user)
#
#                 f = request.POST.get('type')
#
#                 if f == 'student':
#                     b = StudentProfile(user = user)
#
#                     b.save()
#                     group = Group.objects.get(name="student")
#                     user.groups.add(group)
#                 if f == 'teacher':
#
#                     b = Teacher(name = user)
#                     b.save()
#                     group = Group.objects.get(name="teacher")
#                     user.groups.add(group)
#
#                 return redirect('login')
#
#         context = {'form': form}
#         return render(request , 'front/register.html', context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                if request.user.is_staff:
                    return redirect('dashboard')
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request , 'login.html', context)

@login_required(login_url = '/login/')
def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url = '/login/')
def dashboard(request):

    return render(request, 'back/dashboard.html')
