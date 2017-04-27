from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import LoginForm, NewUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from search.models import *

# login page view
def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('profile')
            else:
                return HttpResponse("not a user")
        else:
            return HttpResponse("invalid form")
    else:
        form = LoginForm()
    return render(request,'search/index.html',{'form':form})

# profile page view
def profile(request):
    user = request.user
    return HttpResponse("This is the profile for user %s." %user.id)

# search page view
def query(request):
    template = loader.get_template('search/search.html')
    type_list = Ing_Type.objects.all()
    ingredient_list = Ingredient.objects.all()
    context ={
        'type_list': type_list,
        'ingredient_list': ingredient_list
    }
    return HttpResponse(template.render(context,request))

# sign-up page view
def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user.authenticate(username=username, password=password)
            if user is None:
                user = User.objects.create_user(username,email,password)
                user.firs_name = first_name
                user.last_name = last_name
                user.save()
                return render("Signed-up")
            else: 
                return render("already registered")
        else:
            return render("invalid")
    else:
        form = NewUserForm()
    return render(request,'search/signup.html',{'form':form})

# logout
def logout_view(request):
    logout(request)