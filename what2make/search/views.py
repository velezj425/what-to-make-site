from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import LoginForm, NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from search.models import *
from googleapiclient.discovery import build


# login page view
def index(request):
    if request.user.is_authenticated():
        return redirect('profile')
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
    if request.user.is_authenticated():
        user = request.user
        for profile in Profile.objects.all():
            if profile.user == user:
                user_profile = profile
        saved_list = user_profile.saved.all()
        block_list = user_profile.blocked.all()
        template = loader.get_template('search/profile.html')
        context = {
            'user': user,
            'saved_list': saved_list,
            'block_list': block_list
        }
        return HttpResponse(template.render(context,request))
    else:
        return redirect('index')

# edit profile view
def edit_profile(request):
    if request.user.is_authenticated():
        user = request.user
        for profile in Profile.objects.all():
            if profile.user == user:
                user_profile = profile
        template = loader.get_template('search/editProfile.html')
        type_list = Ing_Type.objects.all()
        ing_list = Ingredient.objects.all()
        context = {
            'profile': user_profile,
            'saved_recipes': user_profile.saved.all(),
            'type_list': type_list,
            'ing_list': ing_list,
            'block_list': user_profile.blocked.all()
        }
        return HttpResponse(template.render(context,request))
    else:
        return redirect('index')

# search page view
def query(request):
    if request.user.is_authenticated():
        user = request.user
        for profile in Profile.objects.all():
            if profile.user == user:
                user_profile = profile
        block_list = user_profile.blocked.all()
        template = loader.get_template('search/search.html')
        type_list = Ing_Type.objects.all()
        ingredient_list = Ingredient.objects.all()
        context ={
            'block_list': block_list,
            'type_list': type_list,
            'ingredient_list': ingredient_list
        }
        return HttpResponse(template.render(context,request))
    else:
        return redirect('index')

# search result page
def result(request):
    if request.user.is_authenticated() and request.method == 'POST':
        service = build("customsearch", "v1", developerKey="AIzaSyATAPIGxR0mMdd6XM7QAjg5zfFcONRBNGU")
        user = request.user
        for profile in Profile.objects.all():
            if profile.user == user:
                user_profile = profile
        block_list = user_profile.blocked.all()
        template = loader.get_template('search/result.html')
        qry = ""
        ing_list = request.POST.getlist('ing_list')
        for ing in ing_list:
            qry = qry + " '" + ing.name + "'"
        for ing in block_list:
            qry = qry + " '-" + ing.name + "'"
        results = service.cse().list(q=qry, cx='006834900479128639157:ow0w0hxfk7m').execute()
        links = []
        for res in results:
            links.append(res.get('link'))
        context = {
            'results': links,
            'profile': user_profile 
        }
        return HttpResponse(template.render(context,request))
    elif request.user.is_authenticated():
        return redirect('query')
    else:
        return redirect('index')

# sign-up page view
def signup(request):
    if request.user.is_authenticated():
        return redirect('profile')
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user = authenticate(username=username, password=password)
            if user is None:
                user = User.objects.create_user(username,email,password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                user = authenticate(username=username, password=password)
                login(request,user)
                profile = Profile(user=user)
                profile.save()
                return redirect('profile')
            else: 
                return redirect('index')
        else:
            return redirect('signup')
    else:
        form = NewUserForm()
    return render(request,'search/signup.html',{'form':form})

# logout
def logout_view(request):
    logout(request)
    return redirect('index')