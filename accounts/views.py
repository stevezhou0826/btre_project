from django.contrib import messages
from django.shortcuts import redirect, render


# Create your views here.
def register(request):
    if request.method == 'POST':
        # Register User
        messages.error(request, 'Testing Error Message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # Login User
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashbaord.html')