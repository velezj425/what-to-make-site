from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
    return HttpResponse("This is a sign-in page!")