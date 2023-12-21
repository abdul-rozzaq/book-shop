from django.shortcuts import render,redirect
from accounts.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required



def register(request):
    context = {
        'messages': [],
    }
    messages = context['messages']
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm_password')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.append('Email already used')
            
            elif User.objects.filter(username=username).exists():
                messages.append('Username already used')
            
            else:
                user = User.objects.create(username=username, email=email)
                
                user.set_password(password)
                user.save()
                
                return redirect('login')                
        else:
            messages.append('Passwords do not match')
    
    
    return render(request, 'accounts/register.html', context)



def login(request):
    context = {
        'messages': [],
    }
    messages = context['messages']
    
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.append('Invalid username or password. Please try again.')
        else:
            messages.append('Username and password are required.')
    
    print(context)
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('home') 

@login_required
def profile_page(request):
    return render(request, 'profile.html')