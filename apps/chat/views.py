from django.shortcuts import render
from . models import Message
from django.http import HttpResponse


def home(request):
    messages = Message.objects.all()
    return render(request, 'index.html', {'messages': messages})