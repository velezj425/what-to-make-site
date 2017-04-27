from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import LoginForm, NewUserForm
from django.contrib.auth.decorators import login_required

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/signup/')
    form = LoginForm(request.POST or None)
    return render(request,'search/index.html',{'form':form})

@login_required
def profile(request, profile_id):
    return HttpResponse("This is the profile for user %s." %profile_id)

@login_required
def query(request, profile_id):
    return HttpResponse("This is the search page.")

@login_required
def result(request, profile_id):
    return HttpResponse("This is the result page.")

def signup(request):
    form = NewUserForm(request.POST or None)
    return render(request,'search/signup.html',{'form':form})

def logout_view(request):
    logout(request)