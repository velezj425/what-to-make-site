from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import LoginForm, NewUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return render(request,'search/search.html')
            else:
                return HttpResponse("not a user")
        else:
            return HttpResponse("invalid form")
    else:
        form = LoginForm()
    return render(request,'search/index.html',{'form':form})

def profile(request, profile_id):
    return HttpResponse("This is the profile for user %s." %profile_id)

def query(request):
    return render(request, 'search/search.html')

def result(request, profile_id):
    return HttpResponse("This is the result page.")

def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user = User.objects.create_user(username,email,password)
            user.firs_name = first_name
            user.last_name = last_name
            user.save()
            return render("Signed-up")
        else:
            return render("invalid")
    else:
        form = NewUserForm()
    return render(request,'search/signup.html',{'form':form})

def logout_view(request):
    logout(request)