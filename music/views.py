from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Album, Song
from django.urls import reverse

def index(request):
    album_list = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'album_list': album_list,
    }
    return render(request, 'music/index.html', {'album_list': album_list})



def detail(request, album_id):
    album_details = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album_details': album_details})

def favorite(request,album_id):
    album_details = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album_details.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'music/detail.html', {
            'album_details': album_details,
            'error_message': "You didn't select a song.",
        })
    else:
        selected_song.favorite = True
        selected_song.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('music:detail', args=(album_details.id,)))
