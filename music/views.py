from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Music App  index.")


def favorite(request):
    return HttpResponse("Hello, world. You're at the Music/Favorite App  index.")


