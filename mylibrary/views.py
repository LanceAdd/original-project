# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from . import models
# Create your views here.
def Index(request):
	book = models.Book_list.objects.all()
	return render(request,'mylibrary/index.html',{'book':book})

def Index2(request,bookuser_id):
	book = models.Book_list.objects.all()
	user = models.User.objects.get(pk=bookuser_id)
	return render(request,'mylibrary/index.html',{'book':book,'bookuser':user})

def Reach_login(request):
	return render(request,'mylibrary/login.html')

def Login(request):
	username = request.POST.get('user','0')
	userpassword = request.POST.get('password','0')
	user = models.User.objects.filter(user=username,password=userpassword)
	if user:
		booksuser = models.User.objects.get(user=username)
		book = models.Book_list.objects.all()
		return render(request,'mylibrary/index.html',{'bookuser':booksuser,'book':book})
	else:
		return render(request,'mylibrary/loginfailed.html')

def Reach_register(request):
	return render(request,'mylibrary/register.html')

def Register(request):
	user = request.POST.get('user','0')
	password = request.POST.get('user','0')
	create_user = models.User.objects.create(user=user,password=password)
	return render(request,'mylibrary/registersuccess.html')

def Show(request,book_id,bookuser_id):
	books = models.Book_list.objects.get(pk=book_id)
	bookuser = models.User.objects.get(pk=bookuser_id)
	return render(request,'mylibrary/show.html',{'book':books,'bookuser':bookuser})

def Namesearch(request):
	book_name = request.POST.get('bookname','0')
	userid = request.POST.get('userid','0')
	bookuser = models.User.objects.get(pk=userid)
	books = models.Book_list.objects.get(bookname=book_name)
	return render(request,'mylibrary/findresault.html',{'book':books,'bookuser':bookuser})

def Authorsearch(request):
	book_author = request.POST.get('bookauthor')
	userid = request.POST.get('userid','0')
	bookuser = models.User.objects.get(pk=userid)
	books = models.Book_list.objects.get(bookauthor=book_author)
	return render(request,'mylibrary/findresault.html',{'book':books,'bookuser':bookuser})

def Borrow_book(request,book_id,bookuser_id):
	books = models.Book_list.objects.get(pk=book_id)
	bookuser = models.User.objects.get(pk=bookuser_id)
	return render(request,'mylibrary/borrowconfirm.html',{'book':books,'bookuser':bookuser})

def Borrow_confirm(request):
	booksname = request.POST.get('bookname','0')
	booksauthor = request.POST.get('bookauthor','0')
	users = request.POST.get('user','0')
	bookuser = models.User.objects.get(pk=users)
	result = models.Borrow_history.objects.create(bookuser=bookuser.user,bookname=booksname,bookauthor=booksauthor)
	'''
	findborrow = models.Borrow_history.objects.filter(bookuser=bookuser.user,bookname=booksname,bookauthor=booksauthor)
	findback = models.Back_history.objects.filter(bookuser=bookuser.user,bookname=booksname,bookauthor=booksauthor)
	list1=[]
	for x in range(len(findborrow)):
		print type(findborrow[x])
		print findborrow[x].id
		list1.append(findborrow[x].id)
	max_id1 = max(list1)
	list2=[]
	for y in range(len(findback)):
		list2.append(findback[y].id)
	max_id2 = max(list2)
	lastborrow = models.Borrow_history.objects.get(pk=max_id1)
	lastback = models.Back_history.objects.get(pk=max_id2)
	if lastborrow.time<lastback.time:
		result = models.Borrow_history.objects.create(bookname=booksname,bookauthor=booksauthor,bookuser=bookuser.user,stata=1)
		return render(request,'mylibrary/borrowsuccess.html',{'bookuser':bookuser})
	else:
		return render(request,'mylibrary/borrowfailed.html',{'bookuser','bookuser'})
	'''
	if result:
		return render(request,'mylibrary/borrowsuccess.html',{'bookuser':bookuser})
	else:
		return render(request,'mylibrary/borrrowfailed.html',{'bookuser':bookuser})

def Back_book(request,book_id,bookuser_id):
	book = models.Book_list.objects.get(pk=book_id)
	bookuser = models.User.objects.get(pk=bookuser_id)
	return render(request,'mylibrary/backconfirm.html',{'book':book,'bookuser':bookuser})

def Back_confirm(request):
	booksname = request.POST.get('bookname','0')
	booksauthor =request.POST.get('bookauthor','0')
	users = request.POST.get('user','0')
	bookuser = models.User.objects.get(pk=users)
	result = models.Back_history.objects.create(bookuser=bookuser.user,bookname=booksname,bookauthor=booksauthor)
	'''
	findborrow = models.Borrow_history.objects.filter(bookuser=bookuser.user,bookname=booksname,bookauthor=booksauthor)
	findback = models.Back_history.objects.filter(bookuser=bookuser.user,bookname=booksname,bookauthor=booksauthor)
	list1=[]
	for x in range(len(findborrow)):
		list1.append(findborrow[x].id)
	max_id1 = max(list1)
	list2=[]
	for y in range(len(findback)):
		list2.append(findback[y].id)
	max_id2 = max(list2)
	lastborrow = models.Borrow_history.objects.get(pk=max_id1)
	lastback = models.Back_history.objects.get(pk=max_id2)
	if lastborrow.time>lastback.time:
		result = models.Back_history.objects.create(bookname=booksname,bookauthor=booksauthor,bookuser=bookuser.user,stata=1)

		return render(request,'mylibrary/backsuccess.html',{'bookuser':bookuser})
	else:
		return render(request,'mylibrary/backfailed.html',{'bookuser':bookuser})
	'''
	if result:
		return render(request,'mylibrary/backsuccess.html',{'bookuser':bookuser})
	else:
		return render(request,'mylibrary/backfailed.html',{'bookuser':bookuser})

def Showhistory(request,bookuser_id):
	history1 = models.Borrow_history.objects.all()
	history2 = models.Back_history.objects.all()
	user = models.User.objects.get(pk=bookuser_id)
	return render(request,'mylibrary/showhistory.html',{'borrowhistory':history1,'backhistory':history2,'bookuser':user})

def Loginout(request):
	return render(request,'mylibrary/index.html')