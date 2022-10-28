from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models



class Album(models.Model):
    artiste = models.Charfield(max_length=250)
    album_title = models.Cahrfield(max_length=500)
    lyrics = models.CharField(max_length=100)
    song = models.CharField(max_length=1000)
    
    
    class CommonInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class musician(CommonInfo):
    home_group = models.CharField(max_length=5)
    
        