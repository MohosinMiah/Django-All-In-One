from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Album


def index(request):
    album_list = Album.objects.all()
    # template = loader.get_template('music/index.html')
    context = {
        'album_list': album_list,
    }
    return render(request, 'index.html', {'album_list': album_list})
def favorite(request):
    return HttpResponse("Hello, world. You're at the Music/Favorite App  index.")

def detail(request, album_id):
    return HttpResponse("You're looking at question %s." % album_id)

