from django.http import HttpResponse
from django.shortcuts import render
from album.models import Picture, Comment

def index(request):
    picture_list = Picture.objects.all()
    context = { 'picture_list' : picture_list }
    return render(request, 'album/index.html', context)

def detail(request, picture_id):
    return HttpResponse("You're looking at picture %s." % picture_id) 
