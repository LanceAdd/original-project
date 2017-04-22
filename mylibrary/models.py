# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import dateformat

# Create your models here.
class Book_list(models.Model):
	bookname = models.CharField(max_length=32,default='bookname')
	bookauthor = models.TextField(null=True)

class User(models.Model):
	user = models.CharField(max_length=20,default='user')
	password = models.TextField(max_length=20)

class Borrow_history(models.Model):
	bookname = models.CharField(max_length=32,default='bookname')
	bookauthor = models.TextField(null=True)
	time = models.DateTimeField(auto_now_add=True)
	stata = models.IntegerField(null=True)
	bookuser = models.CharField(max_length=32)

class  Back_history(models.Model):
	bookname = models.CharField(max_length=32,default='bookname')
	bookauthor = models.TextField(null=True)
	time = models.DateTimeField(auto_now_add=True)
	stata = models.IntegerField(null=True)
	bookuser = models.CharField(max_length=32)
