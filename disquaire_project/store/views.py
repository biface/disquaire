# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    message = "Salut, tout le monde !"
    return HttpResponse(message)

from .models import ALBUMS

def listing(request):
    albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)
