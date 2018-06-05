# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import images, user
from django.contrib import messages
import bcrypt
# Create your views here.
def main(request):
    context = {
        'images': images.objects.all().order_by('-id'),
        'string': "Interested in spesific types of art? use the art dropdown menu to filter results.",
        'type': 0
    }
    return render(request, 'benart/main.html', context)

def contact(request):
    return render(request, 'benart/contact.html')
def about(request):
    return render(request, 'benart/aboutme.html')
def paint(request):
    if 'email' in request.session: 
        context = {
            'images': images.objects.all().order_by('-id'),
            'string': "Paintings",
            'type': 1
        }
        return render(request, "benart/main.html", context)
    else:
        return redirect(login)
def draw(request):
    if 'email' in request.session: 
        context = {
            'images': images.objects.all().order_by('-id'),
            'string': "Drawings",
            'type': 2
        }
        return render(request, "benart/main.html", context)
    else:
        return redirect(login)
def threed(request):
    if 'email' in request.session: 
        context = {
            'images': images.objects.all().order_by('-id'),
            'string': "3d Art",
            'type': 3
        }
        return render(request, "benart/main.html", context)
    else:
        return redirect(login)
def game(request):
    if 'email' in request.session: 
        context = {
            'images': images.objects.all().order_by('-id'),
            'string': "Game Art",
            'type': 4
        }
        return render(request, "benart/main.html", context)
    else:
        return redirect(login)
def login(request):
    return render(request, "benart/login.html")
def validate_login(request):
    if request.method == 'POST':
        errors = user.objects.log_in(request.POST)
        if errors and len(errors):
            for tag, errors in errors.iteritems():
                messages.error(request, errors, extra_tags=tag)
            return redirect(login)
        else:
            users = user.objects.filter(email=request.POST['email'])
            request.session['email'] = request.POST['email']
            request.session['username'] = users[0].user_name
            return redirect(main)
def registration(request):
    return render(request, "benart/registration.html")
def register(request):
    if request.method == 'POST':
        errors = user.objects.registration_validator(request.POST)
        if len(errors):
            for tag, errors in errors.iteritems():
                messages.error(request, errors, extra_tags=tag)
            return redirect(registration)
        else:
            hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            user.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'],phone = request.POST['phone'], user_name = request.POST['username'], email=request.POST['email'], password = hash1, user_level=0)
        return redirect(main)