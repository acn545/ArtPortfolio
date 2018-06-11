# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re, bcrypt
# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# UserManager takes care of the login and registrations validations
class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors['first_name'] = "Please enter a valid first name"
        if len(postData['last_name']) < 1:
            errors['last_name'] = "Please enter a valid last name"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Please enter a valid email address"
        if len(postData['password']) < 8:
            errors['password'] = "please enter a password of atleast 8 characters"
        if postData['password'] != postData['cpassword']:
            errors['match'] = 'Passwords did not match please try again'
        return errors
    def log_in(self, postData):
        errors={}
        users = user.objects.filter(email= postData['email'])
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Please Enter a Valid Email Address"
            return errors
        if postData['email'] != users[0].email:
            errors['notfound'] = "Email Address is not registered"
            return errors;
        if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()) == False:
            errors['password'] = 'incorrect password entered'
            return errors
# database model for image location strings
class images(models.Model):
    id = models.AutoField(primary_key = True)
    img = models.CharField(max_length = 255)
    allimg = models.IntegerField()
    type = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
#database model for registered users.
class user(models.Model):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 255)
    user_name = models.CharField(max_length = 255)
    user_level = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
#database Model for adding comments
class comment(models.Model):
    comment = models.TextField(max_length = 1000)
    images = models.ForeignKey('images', related_name='comments')
    user = models.ForeignKey('user', related_name='comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)