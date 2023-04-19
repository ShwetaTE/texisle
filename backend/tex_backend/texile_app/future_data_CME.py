from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
import requests
import urllib.request
import json
import time
from datetime import datetime, timedelta, date

# API to push data from CME group after it is pulled on azure functions
@api_view(['POST'])
def future_data_push(request):
    final_data = request.data["data"]
    print(type(final_data))
    ticker = request.data["chart"]
    print(ticker)
    # print(final_data)
    future_yahoo_data.objects.filter(chart = ticker).delete()
    for n in final_data:
        # print(n)
        future_obj = future_yahoo_data(chart = ticker , data = float(n[0]), date = n[1])
        future_obj.save()
    return Response({"status":200})

##############################################################################
#DEPRICATED
# API to pull data from CME group
@api_view(['GET'])
def future_data_pull_CME(request):
    code_list= [['iron','5214'],['scrap','6788'],['hrc','2508'],['MFFH22.NYM','5941'],['ULSD','4899']]  #,['HO=F','426'],['RB=F','429']
    for each in code_list:
        try:
            f_data=cme_data(each[1])
            test_list = f_data
            res= []
            for i in test_list:
                if i not in res:
                    res.append(i)
            data_push(res, each[0])
        except:
            url = "http://localhost:8000/texisle-app/send_mail/"
            payload={'content': 'Issue with CME future data pull for '+each[0]}
            response = requests.request("POST", url, headers={}, data=payload, files={})
    
    return Response({"status":200})

def cme_data(code):
    url = "https://www.cmegroup.com/CmeWS/mvc/Quotes/Future/"+code+"/G"
    page=urllib.request.Request(url,headers={'User-Agent': 'PostmanRuntime/7.28.4'}) 
    infile=urllib.request.urlopen(page).read()
    data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
    data = data.replace('<br />','' )
    data1= json.loads(data)
    quotes = data1["quotes"]
    data_list = []
    for each in quotes:
        temp = [(each["priorSettle"]), (each["expirationMonth"])]
        data_list.append(temp)
    date = datetime.today().date()
    day = date.strftime("%d")
    for each in data_list:
        try:
            each[1] = datetime.strptime(day+" " + each[1], '%d %b %Y')
            each[1] = each[1].strftime('%m/%d/%Y')
        except:
            try:
                date1 = datetime.today().date()
                date1 = date1 - timedelta(1)
                d = date1.strftime("%d")
                each[1] = datetime.strptime(d+" " + each[1], '%d %b %Y')
                each[1] = each[1].strftime('%m/%d/%Y')
            except:
                date1 = datetime.today().date()
                date1 = date1 - timedelta(3)
                d = date1.strftime("%d")
                each[1] = datetime.strptime(d+" " + each[1], '%d %b %Y')
                each[1] = each[1].strftime('%m/%d/%Y')
    list1=data_list[:24]
    date_list=[]
    val = list1[0][0]
    # print(val)

    date_temp = datetime.now()
    for n in range(0,6):
        temp = date_temp.strftime('%m/%d/%Y')
        date_list.append(temp)
        date_temp = date_temp + timedelta(1)
    # date_list
    final_list = []
    for each in date_list:
        temp=[val, each]
        final_list.append(temp)
    # final_list

    final_list = final_list + list1
    return(final_list)

def data_push(final_data, ticker):
    future_yahoo_data.objects.filter(chart = ticker).delete()
    for n in final_data:
        future_obj = future_yahoo_data(chart = ticker , data = float(n[0]), date = n[1])
        future_obj.save()
    print(ticker + " done")
