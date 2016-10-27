from django.shortcuts import render
from django.http import HttpResponse
import json 
import requests



def connect(request):
#   email="ernipunarora@gmail.com"
#   password="icancode23"
#   headers={'Accept': '*/*',
# 'apikey': 'WeavedDemoKey$2015',
# 'accept-encoding': 'gzip, deflate',}
#   login=requests.get
    check=False
    
    try:
        statusi=request.POST['radio']
        speed=request.POST['radio']
        check=True

    except:
        print "there was an error"

    HttpResponse("<html><h1>hey there</h1></html>")
    deviceadd='80:00:00:05:46:01:F5:40'
    paddr=routine(deviceadd)
    if (check):
        communicate(paddr,statusi,speed)

    else:
        return render(request,"api/base.html")

    return render(request,"api/base.html")

def routine(dadd):
    t=connectweave()
    getproxy(dadd,t)
    # return proxyaddr

def connectweave():
    email="ernipunarora@gmail.com"
    password="icancode23"
    url='https://api.weaved.com/v22/api/user/login/%s/%s'%(email,password)
    headers={'Accept': '*/*',
    'apikey': 'WeavedDemoKey$2015',
    'accept-encoding': 'gzip, deflate',}
    login=requests.get(url=url,headers=headers)
    p=login.json()
    return p['token']

def getproxy(devadd,token1):
    ip=requests.get(url='http://ip.42.pl/raw').text
    param={
    "deviceaddress": "80:00:00:05:46:01:F5:40",
    "hostip": ip,
    "wait": "True"}
    
    head={"Accept": "*/*",
    "apikey": "WeavedDemoKey$2015",
    "token": token1,
    "accept-encoding": "gzip, deflate",
    "content-type": "application/json",
    "content-length": "82"
    }
    pro=requests.post(url='https://api.weaved.com/v22/api/device/connect',headers=head,data=json.dumps(param))
    p=pro.json()
    print p['connection']['proxy'] + '/control.php'


def communicate(paddr,statusi,speed):
    par={
    "status":statusi,
    "speed":speed,
    }
    head={'Content-Type': 'application/json'}
    req=requests.post(url=paddr,headers=json.dumps(head),data=json.dumps(par))



# Create your views here.
