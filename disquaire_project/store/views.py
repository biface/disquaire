#from django.http import HttpResponse
#from django.template import loader
#
#from .models import Album, Artist, Contact, Booking
#
#
#def index(request):
#    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
#    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
#    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
#    template = loader.get_template('store/index.html')
#    context = {
#        'albums': albums
#    }
#    return HttpResponse(template.render(context, request))
#
#def listing(request):
#    albums = Album.objects.filter(available=True)
#    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
#    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
#    return HttpResponse(message)
#
#def detail(request, album_id):
#    album = Album.objects.get(pk=album_id)
#    artists = " ".join([artist.name for artist in album.artists.all()])
#    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album.title, artists)
#    return HttpResponse(message)
#
#def search(request):
#    query = request.GET.get('query')
#    if not query:
#        albums = Album.objects.all()
#    else:
#        # title contains the query is and query is not sensitive to case.
#        albums = Album.objects.filter(title__icontains=query)
#
#    if not albums.exists():
#        albums = Album.objects.filter(artists__name__icontains=query)
#
#    if not albums.exists():
#        message = "Misère de misère, nous n'avons trouvé aucun résultat !"
#    else:
#        albums = ["<li>{}</li>".format(album.title) for album in albums]
#        message = """
#            Nous avons trouvé les albums correspondant à votre requête ! Les voici :
#            <ul>{}</ul>
#        """.format("</li><li>".join(albums))
#
#    return HttpResponse(message)

from django.shortcuts import render

from .models import Album, Artist, Contact, Booking


def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    context = {
        'albums': albums
    }
    return render(request, 'store/index.html', context)

def listing(request):
    albums = Album.objects.filter(available=True)
    context = {
        'albums': albums
    }
    return render(request, 'store/listing.html', context)

def detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    artists = [artist.name for artist in album.artists.all()]
    artists_name = " ".join(artists)
    context = {
        'album_title': album.title,
        'artists_name': artists_name,
        'album_id': album.id,
        'thumbnail': album.picture
    }
    return render(request, 'store/detail.html', context)

def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        # title contains the query is and query is not sensitive to case.
        albums = Album.objects.filter(title__icontains=query)
    if not albums.exists():
        albums = Album.objects.filter(artists__name__icontains=query)
    title = "Résultats pour la requête %s"%query
    context = {
        'albums': albums,
        'title': title
    }
    return render(request, 'store/search.html', context)