from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from accounts.forms import UserForm,UserProForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

def index(request):
    return render(request,'base.html')

def register(request):


    registered = False
    profile_form = UserProForm()

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_pic = UserProForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProForm()
    return render(request,'accounts/registration.html',
                            {'registered':registered,
                            'user_form':user_form,
                            'profile_form':profile_form
                                })


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account is Not Active ")
        else:
            return HttpResponse("Use the Correct ID and Password ")
    else:
        return render(request,'accounts/login.html')



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
