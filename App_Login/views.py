from django.shortcuts import render
from App_Login.models import UserProfile
#for user create and login form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Login.forms import SignUpForm, UserProfileUpdateForm, ProfilePic

# Create your views here.
def signUp(request):
    form = SignUpForm()
    registered = False
    if request.method == "POST":
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            registered=True
    diction = {
        'form':form,
        'registered':registered
    }
    return render(request, 'App_Login/signup.html', context=diction)

def signin(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    diction = {
        'form':form
    }
    return render(request, 'App_Login/login.html', context=diction)

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def user_profile(request):
    diction={}
    return render(request, 'App_Login/profile.html', context=diction)

@login_required
def user_change(request):
    current_user = request.user
    form = UserProfileUpdateForm(instance=current_user)
    if request.method == "POST":
        form = UserProfileUpdateForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileUpdateForm(instance=current_user)
    diction={
        'form':form
    }
    return render(request, 'App_Login/change_profile.html', context=diction)

@login_required
def pass_change(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)
    if request.method == "POST":
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
    diction={
        'form':form
    }
    return render(request, 'App_Login/pass_change.html', context=diction)

@login_required
def add_pro_pic(request):
    form = ProfilePic()
    if request.method == "POST":
        form = ProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    diction = {
        'form':form
    }
    return render(request, 'App_Login/pro_pic_add.html', context=diction)

@login_required
def changeProPic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    diction = {
        'form':form
    }
    return render(request, 'App_Login/pro_pic_add.html', context=diction)
