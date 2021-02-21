from django.db import models


# Create your models here.

class Artist(models.Model):

    class Meta:
        verbose_name = "artiste"

    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Contact(models.Model):

    class Meta:
        verbose_name = "prospect"

    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Album(models.Model):

    class Meta:
        verbose_name = "disque"

    reference = models.IntegerField('référence', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    picture = models.URLField()
    artists = models.ManyToManyField(Artist, related_name='album', blank=True)

    def __str__(self):
        return self.title


class Booking(models.Model):

    class Meta:
        verbose_name = "réservation"

    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact.name
