# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import images, drawings, paintings, gameArt, art3d
# Create your views here.
def main(request):
    context = {
        'images': images.objects.all(),
        'string': "Interested in spesific types of art? use the art dropdown menu to filter results."
    }
    return render(request, 'benart/main.html', context)

def contact(request):
    return render(request, 'benart/contact.html')
def about(request):
    return render(request, 'benart/aboutme.html')
def paint(request):
    context = {
        'images': paintings.objects.all(),
        'string': "Paintings"
    }
    return render(request, "benart/main.html", context)
def draw(request):
    context = {
        'images': drawings.objects.all(),
        'string': "Drawings"
    }
    return render(request, "benart/main.html", context)
def threed(request):
    context = {
        'images': art3d.objects.all(),
        'string': "3d Art"
    }
    return render(request, "benart/main.html", context)
def game(request):
    context = {
        'images': gameArt.objects.all(),
        'string': "Game Art"
    }
    return render(request, "benart/main.html", context)
def login(request):
    return render(request, "benart/login.html")