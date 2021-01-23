# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    message = "Salut, tout le monde !"
    template = loader.get_template('store/index.html')
    return HttpResponse(template.render(request=request))

