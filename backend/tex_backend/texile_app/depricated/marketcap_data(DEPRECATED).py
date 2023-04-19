from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
from django.core import serializers
from django.utils import timezone
import requests
from typing import final
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re, time
import yfinance as yf
from pandas_datareader import data
from random import randint, randrange
from datetime import datetime, timedelta, date
import pandas_market_calendars as mcal
from datetime import datetime, timedelta, date
import pandas as pd
import numpy as np
import urllib.request
import json
#############################################################################################
# functions no longer in use

def fetch_market_cap_data(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    final_data = []

    data = soup.find_all('table',class_="histDataTable")
    print(data)
    for each in data:
        for n in each.find_all('tr'):
            temp=[]
            data_1 = n.find('td',class_="col1")
            data_2 = n.find('td',class_="col2")
            print(data_1)
            print(data_2)
            try:
                # print(data_1.text.strip())
                data_1 = convert_date(data_1.text.strip())
                data = float(data_2.text.strip()[:-1])
                if(data_2.text.strip()[-1] == 'B'):
                    data = data*1000
                    # print(data)
                # print("data- ", data)
                temp = [data_1, round(data,2)]
                # print(temp)
                final_data.append(temp)
            except:
                continue
    print("final ",final_data)
    return(final_data)

def convert_date(date):
    # date = 'Sept. 26, 2021'
    month = date.split()[0]
    if month == 'Sept.':
        date = date.replace("Sept.","Sep.")
    if month == 'July':
        date = date.replace("July.","Jul.")
    date = re.sub('\W+',' ', date ) + ' 12:00AM'
    # print(date)
    datetime_object = datetime.strptime(date, '%b %d %Y %I:%M%p')
    datetime_object = datetime_object.strftime('%m/%d/%Y')
    # print(datetime_object)
    return(datetime_object)

def market_cap_pull(request):
    list = request
    print(list)
    final_list = []
    market_cap_t = 0
    for each in list:
        temp = []
        print("Pulling data for ",each)
        url = "https://ycharts.com/companies/"+ each +"/market_cap"
        temp = fetch_market_cap_data(url)
        final_list.append(temp)
        market_cap=int(data.get_quote_yahoo(each)['marketCap'])
        # print(market_cap)
        market_cap_t = market_cap_t + market_cap
    # print(final_list)
    temp = final_list[0]
    # print(market_cap_t)
    final_list.pop(0)
    # print(final_list)
    for each in final_list:
        l = len(temp)
        for i in range(0, l):
            temp[i][1] = float(temp[i][1]) + float(each[i][1])
            temp[i][1] = round(temp[i][1],2)
    print(temp)
    return(temp)

# push all data into the database from ychart site
@api_view(['GET'])
def market_cap_data_all(request):
    # STEEL MARKET
    list = ["CMC","GGB"]
    # list = ["CMC","X"]
    temp = market_cap_pull(list)
    # print(temp)
    market_cap_data.objects.filter(chart = "steel market").delete()
    for n in temp:
        # print(n[1])
        market_cap_obj = market_cap_data(chart = "steel market" , data = n[1], date = n[0])
        market_cap_obj.save()
    print(temp[0][1])
    print(temp[1][1])
    print(temp[1][1])
    diff = round(((temp[0][1]-temp[1][1])/temp[1][1])*100,2)
    # print(temp[0][1])
    # print(diff)
    temp1 = temp[0][1]
    l = len(str(temp1))
    print(l)
    if l>4:
        temp1 = temp1/1000
    stock_data.objects.filter(chart_type = "steel_market").delete()
    market_cap_obj = stock_data(chart_type = "steel_market" , data = diff, current = temp1)
    market_cap_obj.save()
    print("data pushed into database")

    # # PIPE MANUFACTURING
    # list = ["TS","VLOUF","X","TMST"]
    # # list = ["CMC","X"]
    # temp = market_cap_pull(list)
    # # print(temp)
    # market_cap_data.objects.filter(chart = "pipe manufacturing").delete()
    # for n in temp:
    #     # print(n[1])
    #     market_cap_obj = market_cap_data(chart = "pipe manufacturing" , data = n[1], date = n[0])
    #     market_cap_obj.save()
    # diff = round(((temp[0][1]-temp[1][1])/temp[1][1])*100,2)
    # # print(temp[0][1])
    # # print(diff)
    # temp1 = temp[0][1]
    # l = len(str(temp1))
    # print(l)
    # if l>4:
    #     temp1 = temp1/1000
    # stock_data.objects.filter(chart_type = "pipe_manufacturing").delete()
    # market_cap_obj = stock_data(chart_type = "pipe_manufacturing" , data = diff, current = temp1)
    # market_cap_obj.save()
    # print("data pushed into database")

    # # IRON ORE MINING
    # list = ["RIO","VALE","SXC"]
    # # list = ["CMC","X"]
    # temp = market_cap_pull(list)
    # # print(temp)
    # market_cap_data.objects.filter(chart = "iron ore").delete()
    # for n in temp:
    #     # print(n[1])
    #     market_cap_obj = market_cap_data(chart = "iron ore" , data = n[1], date = n[0])
    #     market_cap_obj.save()
    # diff = round(((temp[0][1]-temp[1][1])/temp[1][1])*100,2)
    # # print(temp[0][1])
    # # print(diff)
    # temp1 = temp[0][1]
    # l = len(str(temp1))
    # print(l)
    # if l>4:
    #     temp1 = temp1/1000
    # stock_data.objects.filter(chart_type = "iron_ore").delete()
    # market_cap_obj = stock_data(chart_type = "iron_ore" , data = diff, current = temp1)
    # market_cap_obj.save()
    # print("data pushed into database")

    # # STEEL MANUFACTURING
    # list = ["MT","PKX","NUE","STLD","RS","CLF","TX","GGB","X","CMC"]
    # # list = ["CMC","X"]
    # temp = market_cap_pull(list)
    # # print(temp)
    # market_cap_data.objects.filter(chart = "steel manufacturing").delete()
    # for n in temp:
    #     # print(n[1])
    #     market_cap_obj = market_cap_data(chart = "steel manufacturing" , data = n[1], date = n[0])
    #     market_cap_obj.save()
    #     diff = round(((temp[0][1]-temp[1][1])/temp[1][1])*100,2)
    # # print(temp[0][1])
    # # print(diff)
    # temp1 = temp[0][1]
    # l = len(str(temp1))
    # print(l)
    # if l>4:
    #     temp1 = temp1/1000
    # stock_data.objects.filter(chart_type = "steel_manufacturing").delete()
    # market_cap_obj = stock_data(chart_type = "steel_manufacturing" , data = diff, current = temp1)
    # market_cap_obj.save()
    # print("data pushed into database")

    return Response({"status":200})


# pull data from database
@api_view(['POST'])
def market_cap_data_chart(request):
    chart = request.data["chart"]
    # chart = "steel market"
    market_cap_obj = market_cap_data.objects.all().filter(chart = chart)
    data = []
    for n in market_cap_obj:
        temp= [n.date, n.data]
        data.append(temp)
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        for j in data:
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        date = i[0] #+ " 00:00:00"
        pattern = '%m-%d-%Y' # %H:%M:%S'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    return Response(final_data)
