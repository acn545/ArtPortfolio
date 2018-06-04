# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import images
# Create your views here.
def main(request):
    context = {
        'images': images.objects.all(),
        'string': "Interested in spesific types of art? use the art dropdown menu to filter results.",
        'type': 0
    }
    return render(request, 'benart/main.html', context)

def contact(request):
    return render(request, 'benart/contact.html')
def about(request):
    return render(request, 'benart/aboutme.html')
def paint(request):
    context = {
        'images': images.objects.all(),
        'string': "Paintings",
        'type': 1
    }
    return render(request, "benart/main.html", context)
def draw(request):
    context = {
        'images': images.objects.all(),
        'string': "Drawings",
        'type': 2
    }
    return render(request, "benart/main.html", context)
def threed(request):
    context = {
        'images': images.objects.all(),
        'string': "3d Art",
        'type': 3
    }
    return render(request, "benart/main.html", context)
def game(request):
    context = {
        'images': images.objects.all(),
        'string': "Game Art",
        'type': 4
    }
    return render(request, "benart/main.html", context)
def login(request):
    return render(request, "benart/login.html")