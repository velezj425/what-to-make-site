from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import LoginForm

def index(request):
    #template = loader.get_template('search/index.html')
    form = LoginForm(request.POST)
    return render(request,'search/index.html',{'form':form})

def profile(request, profile_id):
    return HttpResponse("This is the profile for user %s." %profile_id)

def query(request, profile_id):
    return HttpResponse("This is the search page.")

def result(request, profile_id):
    return HttpResponse("This is the result page.")

def signup(request):
    return HttpResponse("This is the signup page.")