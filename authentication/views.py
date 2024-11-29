from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import RegisterForm, ChangeUserData

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            messages.success(request, 'Account created successfully')
            registerForm = RegisterForm()
        else:
            messages.error(request, 'There was an error creating your account')
    else:
        registerForm = RegisterForm()

    return render(request, 'signup.html', {'form': registerForm,})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            # check kortechi user database e ache kina
            user = authenticate(username=name, password=userpass)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('signin')
    
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Changed successfully')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})


def changePass_without_oldPass(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Changed successfully')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})


def change_profile(request):
    if request.method == 'POST':
        form = ChangeUserData(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully')
            form = ChangeUserData()
        else:
            messages.error(request, 'There was an error creating your account')
    else:
        form = ChangeUserData(instance = request.user)

    return render(request, 'change_profile.html', {'form': form,})