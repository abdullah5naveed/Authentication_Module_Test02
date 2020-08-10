from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

# Create your views here.

def home(request):
    return render(request, 'auth_module/home.html')



def signupuser(request):
    if request.method == 'GET':
        signupData = {'signupform':UserCreationForm}
        return render(request, 'auth_module/signupuser.html', signupData)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                signupData = {'signupform':UserCreationForm, 'error':"Username Must be Unique..."}
                return render(request, 'auth_module/signupuser.html', signupData)

        else:
            signupData = {'signupform':UserCreationForm, 'error':"Password didn't match"}
            return render(request, 'auth_module/signupuser.html', signupData)




def logoutuser(request):
    return render(request, 'auth_module/logoutuser.html')



def loginuser(request):
    return render(request, 'authmodule/loginuser.html')