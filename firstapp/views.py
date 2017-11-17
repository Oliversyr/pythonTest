import json
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
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
	if (count == 'admin' and int(pwd) == 123456 or True):
		# res = {
		# 	'retCode': 'SUCCESS',
		# 	'retMsg': '登录成功',
		# 	'result': '<h1 style="color: red;">账号：%s， 密码：%s</h1>' % (count, pwd)
		# }
		stockList = []
		crawlSite = "http://hq.sinajs.cn/list=s_sh000001"
		res = requests.get(crawlSite)
		data = res.content.decode('gb2312')
		# stockList = data.split(',')
		print(data, 'dataType===',type(data))
		# return HttpResponse(json.dumps(data, ensure_ascii=False))
		myget = getUrlData('https://movie.douban.com/top250')
		res = {
			'retCode': 'SUCCESS',
			'retMsg': '登录成功',
			'result': myget
		}
		return HttpResponse(json.dumps(res, ensure_ascii=False))
	else:
		res = {
			'retCode': 'FAIL',
			'retMsg': '登录失败',
			'result': '<h1>失败</h1><h1 style="color: red;">账号：%s， 密码：%s</h1>' % (count, pwd)
		}
		return HttpResponse(json.dumps(res, ensure_ascii=False))

def getUrlData(url):
	html = requests.get(url).text	
	# soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
	soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
	links = soup.find('ol')
	myList = []
	for movie_li in links.find_all('div', class_='item'):
		myListItem = {
			'index': movie_li.find('em').get_text(),
			'name': movie_li.find('span', class_="title").get_text()
		}
		myList.append(myListItem)
	print(myList)
	return myList

def templatedef(request):
    	
    return HttpResponse()
    
def printerdef(request):
    	
    return HttpResponse()

def templatelist(request):
    	
    mylist = [{
            "eid": 0,
            "isdefault": 1,
            "moduleid": 200030,
            "modulename": "销售记录",
            "ptlid": 1,
            "rptid": 1,
            "rptname": "销售默认模板",
            "rpturl": "saletemplate"
        },
        {
            "eid": 0,
            "isdefault": 0,
            "moduleid": 200030,
            "modulename": "销售记录",
            "ptlid": 1,
            "rptid": 1,
            "rptname": "销售模板002",
            "rpturl": "saletemplate_002"
        },
        {
            "eid": 0,
            "isdefault": 0,
            "moduleid": 200030,
            "modulename": "销售记录",
            "ptlid": 1,
            "rptid": 1,
            "rptname": "销售模板003",
            "rpturl": "saletemplate_003"
        },
        {
            "eid": 0,
            "isdefault": 0,
            "moduleid": 200030,
            "modulename": "销售记录",
            "ptlid": 1,
            "rptid": 1,
            "rptname": "销售模板004",
            "rpturl": "saletemplate_004"
        },
        {
            "eid": 0,
            "isdefault": 0,
            "moduleid": 200030,
            "modulename": "销售记录",
            "ptlid": 1,
            "rptid": 1,
            "rptname": "销售模板005",
            "rpturl": "saletemplate_005"
        }
    ]

    if(request.method == 'GET'):
    	res = {
			'retCode': 'SUCCESS',
			'retMsg': '登录成功',
			'result': mylist
		}
    else:
    	res = {
			'retCode': 'FAIL',
			'retMsg': '登录失败',
			'result': []
		}	
    print(request.method)	
    return HttpResponse(json.dumps(res, ensure_ascii=False));

def printerlist(request):
    mylist = [{
            "name": "打印机001"
        },
        {
            "name": "打印机002"
        },
        {
            "name": "打印机003"
        },
        {
            "name": "打印机004"
        },
        {
            "name": "打印机005"
        }
    ]

    if(request.method == 'GET'):
    	res = {
			'retCode': 'SUCCESS',
			'retMsg': '登录成功',
			'result': mylist
		}
    else:
    	res = {
			'retCode': 'FAIL',
			'retMsg': '登录失败',
			'result': []
		}	
    print(request.method)	
    return HttpResponse(json.dumps(res, ensure_ascii=False));	

def customlist(request):
    with open('frontend/static/custom.json', 'r', encoding='UTF-8') as file:
        alldata = json.loads(file.read())

    if(request.method == 'POST'):
        # keyVal = str(request.POST['key'])
        # clist = alldata['items']
        print(request.POST)
        print(type(request.POST.get('pageNum')))
        newlist = []
        if(request.POST.get('pageNum') == '1'):
            newlist = alldata['items1']
        elif(request.POST.get('pageNum') == '2'):
            newlist = alldata['items2']    
        # for custom in clist:
        #     if(keyVal in custom['ename'] or keyVal in str(custom['coeid'])):
        #         newlist.append(custom)
    
    print(newlist)
    # print(keyVal)

    res = {
        'retCode': 'SUCCESS',
        'retMsg': '操作成功',
        'pageNum': 1 if(len(newlist) == 10) else(2),
        'pageSize': 10,
        'result': newlist,
        'totalrecord': 18
    }
    return HttpResponse(json.dumps(res, ensure_ascii=False))

