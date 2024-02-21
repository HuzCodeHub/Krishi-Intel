from django.shortcuts import render, redirect
from .forms import UserAdminCreationForm
from . forms import LoginForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.db import DatabaseError
from django.contrib import messages


def homepage(request):

    return render(request, 'loginapp/index.html')
           

def signupPage(request):
     try:
      form = UserAdminCreationForm()

      if request.method == "POST":

        form = UserAdminCreationForm(request.POST)

        if form.is_valid():
                      form.save()
                      return redirect('loginPage')
     except DatabaseError as e:
                    messages.error(request,"Email is already taken.")

     context = {'registerform':form}
     return render(request, 'loginapp/signupPage.html', context=context)  



def loginPage(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = form.cleaned_data['password']
            # Authenticate user using email instead of username
            user = authenticate(request, email= email , password=password)

            if user is not None:
                print('asda')
                auth.login(request, user)
                return redirect("dashboard")

    context = {'loginform': form}
    return render(request, 'loginapp/loginPage.html', context=context)


def user_logout(request):
    auth.logout(request)

    return redirect("")


@login_required(login_url="loginPage")
def dashboard(request):
    return render(request, 'loginapp/dashboard.html')
