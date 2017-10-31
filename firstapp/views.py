from django.shortcuts import render

# Create your views here.
# 

#coding:utf-8

from django.http import HttpResponse

def index(request):
	return HttpResponse(u"哈哈哈哈哈哈哈")

def news1(request, year='2015'):
	res = '<h1 style="color: red;">%s</h1>' % year * 3
	return HttpResponse(res)

def login(request):
	count = request.GET['count']
	pwd = request.GET['pwd']
	res = '<h1 style="color: red;">账号：%s， 密码：%s</h1>' % (count, pwd)
	return HttpResponse(res)	