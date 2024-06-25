from django.shortcuts import render
from . models import Message, Room
from django.http import HttpResponse


def home(request):
    rooms = Room.objects.all()
    return render(request, 'chat/home.html', {
        'rooms': rooms
        })
