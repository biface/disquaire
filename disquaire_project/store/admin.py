from django.contrib import admin
from .models import Booking, Contact, Album, Artist

# Register your models here.


class BookingInLine(admin.TabularInline):
    model = Booking
    fieldsets = [
        (None, {'fields': ['album', 'contacted', 'created_at']})
    ]
    readonly_fields = ["created_at"]
    extra = 1
    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"

class AlbumArtistInLine(admin.TabularInline):
    model = Album.artists.through
    extra = 1

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInLine,]

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumArtistInLine,]

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['reference', 'title']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ['created_at', 'contacted']