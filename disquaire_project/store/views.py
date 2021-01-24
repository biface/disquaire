# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Import local ORM Objects

from .models import Album, Artist, Contact, Booking


# Create your views here.

def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    template = loader.get_template('store/index.html')
    context = {'albums': albums}
    return HttpResponse(template.render(context, request=request))
