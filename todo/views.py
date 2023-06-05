from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def home_page(request):
    return render(request, 'index.html')


def signup(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        if password==password2:
            my_user = User.objects.create_user(email, password)
            my_user.save()
            return render(request, 'index.html')
        else:
            return render()
    return render(request, 'signup.html')