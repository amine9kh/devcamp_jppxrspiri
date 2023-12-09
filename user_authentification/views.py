from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from user_authentification.models import UserProfile

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home_view(request):
    # Your view logic for the home page
    return render(request, 'index.html')
def signin_view(request):
    return render(request, 'signin.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user_profile = UserProfile.objects.create(user=user)
        return redirect('chatbot_view')
    else:
        return render(request, 'signin.html')
    

def login_view(request):
    if request.method == 'POST':
        identifier = request.POST['identifier']
        password = request.POST['password']
        # Try to authenticate with identifier as username
        user = authenticate(request, username=identifier, password=password)
        if user is None:
            # Try to authenticate with identifier as email
            try:
                user_obj = User.objects.get(email=identifier)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None
        if user is not None:
            login(request, user)
            return redirect('chatbot_view')
        else:
            messages.error(request, 'Invalid username/email or password.')
            return redirect('login')
    else:
        return render(request, 'signin.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def delete_account(request):
    user = request.user
    user.delete()
    messages.success(request, 'Your account has been deleted.')
    return redirect('register')