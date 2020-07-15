from django.shortcuts import render , get_object_or_404, redirect
from .models import *
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
import datetime
from django.utils.timezone import utc
from django.contrib.auth.models import Group
from main.models import *
# Create your views here.

@login_required(login_url = '/login/')
def home(request):
    usr = request.user.username
    remaining = []
    
    if request.user.is_superuser:
        return render(request, 'front/home.html')
    try:
        usr = StudentProfile.objects.get(user=usr)
        try:
            revset = ReviewSet.objects.filter(semester=usr.year_semester)
            for i in revset:
                if usr not in i.given:
                    remaining.append(i)
        except:
            return render(request, 'front/home.html',{'revset':revset,'remaining':remaining})
    except:
        return render(request, 'front/home.html',{'revset':revset, 'remaining':remaining})

    return render(request, 'front/home.html',{'revset':revset, 'remaining':remaining})

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                messages.success(request, 'Account was created for ' + username)
                print(user)

                f = request.POST.get('type')

                if f == 'student':
                    b = StudentProfile(user = user)

                    b.save()
                    group = Group.objects.get(name="student")
                    user.groups.add(group)
                if f == 'teacher':

                    b = Teacher(name = user)
                    b.save()
                    group = Group.objects.get(name="teacher")
                    user.groups.add(group)

                return redirect('login')

        context = {'form': form}
        return render(request , 'front/register.html', context)
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
        return render(request , 'front/login.html', context)

@login_required(login_url = '/login/')
def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url = '/login/')
def dashboard(request):

    return render(request, 'back/dashboard.html')
