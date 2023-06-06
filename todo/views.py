from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home_page(request):
    
    return render(request, 'index.html')


def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        if password==password2:
            my_user = User.objects.create_user(name, email, password)
            my_user.save()
            return redirect('login') # Redirect to the 'login' URL pattern
        else:
            return HttpResponse('Something wrong with your email')
    return render(request, 'signup.html')


def login_page(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') # Redirect to the 'home' URL pattern
        else:
            return HttpResponse('Invalid credentials')
        
    return render(request, 'login.html')
