from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('search/signin.html')
    return HttpResponse(template.render(request))