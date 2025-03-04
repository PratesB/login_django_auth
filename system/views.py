from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.views.decorators.http import require_http_methods
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
import logging


from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_django, logout as logout_django



logger = logging.getLogger(__name__)

@require_http_methods(['GET'])
def index(request):
    return render(request, 'index.html')




@require_http_methods(['GET', 'POST'])
def create_account(request):
    if request.method=='GET':
        if request.user.is_authenticated:
            return redirect('system')
        
        return render(request, 'create_account.html')

    email = request.POST.get('email')
    password = request.POST.get('password')


    try:
        email_validator = EmailValidator()
        email_validator(email)

        if len(password) < 6:
            messages.error(request, 'Password must be at least 8 characters long')
            return redirect('create_account')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('create_account')
        

        User.objects.create_user(username=email, email=email, password=password)
        messages.success(request, 'Your account has been successfully created. Log in now to begin using the system.')
        return redirect('login')
    

    except ValidationError as e:
        messages.error(request, 'Invalid email. Please try again.')
        logger.error(f'Email validation error: {e}')
        return redirect('create_account')
    
    except Exception as e:
        messages.error(request, 'Registration failed. Please try again.')
        logger.error(f'Registration error: {e}')
        return redirect('create_account')




@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method=='GET':
        if request.user.is_authenticated:
            return redirect('system')
        
        return render(request, 'login.html')
    

    email = request.POST.get('email')
    password = request.POST.get('password')

    if not all([email, password]):
        messages.error(request, 'Fill out all fields before submitting')
        return redirect('login')


    client = authenticate(request, username=email, password=password)

    if client is not None:
        auth.login(request, client)
        logger.info(f'User {email} logged in successfully')
        return redirect('system')
    
    messages.error(request, 'Invalid email or password')
    logger.error((f'Failed login attempt for user: {email}'))
    return redirect('login')



@require_http_methods(['POST'])
@login_required(login_url='login')
def logout(request):
    email = request.user.email
    logout_django(request)
    messages.success(request, 'You have been successfully logged out.')
    logger.info(f'User {email} logged out successfully')
    return redirect('login')





@login_required(login_url='login')
@require_http_methods(["GET"])
def system(request):
    return render(request, 'system.html')