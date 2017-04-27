from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('search/index.html')
    return HttpResponse(template.render(request))

def profile(request, profile_id):
    return HttpResponse("This is the profile for user %s." %profile_id)

def query(request, profile_id):
    return HttpResponse("This is the search page.")

def result(request, profile_id):
    return HttpResponse("This is the result page.")

def signup(request):
    return HttpResponse("This is the signup page.")