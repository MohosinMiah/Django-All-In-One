from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=255)
    genere = models.CharField(max_length=255)
    album_logo = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.album_title +' - '+self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=200)
    song_title =models.CharField(max_length=255)
    def __str__(self):
        return self.song_title + '  - Album Name : '+self.album.album_title
