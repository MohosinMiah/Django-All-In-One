from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Music App  index.")


def favorite(request):
    return HttpResponse("Hello, world. You're at the Music/Favorite App  index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

