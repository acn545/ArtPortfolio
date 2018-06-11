# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import images, user
from django.contrib import messages
import bcrypt

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# renders the main page, displays all art uploaded in the images Db
def main(request):
    context = {
        'images': images.objects.all().order_by('-id'),
        'string': "Interested in spesific types of art? use the art dropdown menu to filter results.",
        'type': 0
    }
    return render(request, 'benart/main.html', context)
# renders the contact page, used to take in random user information to send emails to the portfolio artist
def contact(request):
    return render(request, 'benart/contact.html')
# renders the about page, describing the artist
def about(request):
    return render(request, 'benart/aboutme.html')
# renders main, only shows images with the painting identifier from the Db
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
# renders main, only shows images with the drawing identifier from the Db
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
# renders main, only shows images with the 3D identifier from the Db
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
# renders main, only shows images with the Game design identifier from the Db
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
# renders the login form
def login(request):
    return render(request, "benart/login.html")
# result of login form, runs validation model returns errors/logs users into session.
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
            if users[0].user_level == "9":
                return redirect(simple_upload)
            return redirect(main)
# renders registration form
def registration(request):
    return render(request, "benart/registration.html")
# result of registration form, displays errors/ adds new unique users to the user Db
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
# renders the blog page, where artist can post blogs/users can comment on them
def blog(request):
    if 'email' in request.session: 
        return render(request, "benart/main.html")
    else:
        return redirect(login)
# loged in admin/artists can upload images to the images to the media folder/add file location to images Db
def simple_upload(request):
    if 'email' in request.session: 
        users = user.objects.filter(email=request.session['email'])
        if users[0].user_level == "9":
            if request.method == 'POST' and request.FILES['myfile']:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                images.objects.create(img = uploaded_file_url , allimg = 0 , type = request.POST['type'] )
                return render(request, 'benart/dashboard.html', {'uploaded_file_url': uploaded_file_url})
            return render(request, 'benart/dashboard.html')
    else:
        return redirect(login)