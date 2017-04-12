from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the signin page.")

def profile(request, profile_id):
    return HttpResponse("This is the profile for user %s." %profile_id)