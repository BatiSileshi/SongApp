from django.db import models

# Create your models here.


class Song(models.Model):
    song_title=models.CharField(max_length=200, null=True, blank=True)
    artist_name=models.CharField(max_length=200, null=True, blank=True)
    album=models.CharField(max_length=200, null=True, blank=True)
    cover_image = models.ImageField(null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.song_title