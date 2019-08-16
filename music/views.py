from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Album


def index(request):
    album_list = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'album_list': album_list,
    }
    return render(request, 'music/index.html', {'album_list': album_list})
def favorite(request):
    return HttpResponse("Hello, world. You're at the Music/Favorite App  index.")

def detail(request, album_id):
    album_details = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album_details': album_details})
