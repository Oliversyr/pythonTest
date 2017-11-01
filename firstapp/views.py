import json
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
	print(count, type(count))
	print(pwd, type(pwd))
	if (count == 'admin' and int(pwd) == 123456):
		res = {
			'retCode': 'SUCCESS',
			'retMsg': '登录成功',
			'result': '<h1 style="color: red;">账号：%s， 密码：%s</h1>' % (count, pwd)
		}
		return HttpResponse(json.dumps(res, ensure_ascii=False))
	else:
		res = {
			'retCode': 'FAIL',
			'retMsg': '登录失败',
			'result': '<h1>失败</h1><h1 style="color: red;">账号：%s， 密码：%s</h1>' % (count, pwd)
		}
		return HttpResponse(json.dumps(res, ensure_ascii=False))
		