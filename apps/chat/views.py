from django.shortcuts import render
from . models import Message, Room
from django.http import HttpResponse

rooms = Room.objects.all()

def home(request):
    messages = Message.objects.all()
    return render(request, 'chat/home.html', {
        'messages': messages,
        'rooms': rooms
        })
