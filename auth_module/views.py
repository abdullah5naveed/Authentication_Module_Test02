from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'auth_module/home.html')



def signupuser(request):
    return render(request, 'auth_module/signupuser.html')



def logoutuser(request):
    return render(request, 'auth_module/logoutuser.html')



def loginuser(request):
    return render(request, 'authmodule/loginuser.html')