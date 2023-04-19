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

def fetch_date():
    presentday = datetime.now()
    d = datetime.today().weekday()
    if d == 0:
        date = presentday - timedelta(days = 3)
    else:
        date = presentday - timedelta(days = 1)
    dt = date.strftime('%Y-%m-%d')
    # Create a calendar
    nyse = mcal.get_calendar('NYSE')
    early = nyse.schedule(start_date=dt, end_date=dt)
    date_list = []
    list = mcal.date_range(early, frequency='1D')
    # print(list)
    for each in list:
        dt = each.strftime('%m-%d-%Y')
        date_list.append(dt)
    date_df = pd.DataFrame(date_list, columns =['date'])
    date_df.rename(columns = {'date':'Date'}, inplace = True)
    date_list = date_df.values.tolist()
    return(date_list)

def insert_updated_time(comp):
    dt = datetime.now(tz=timezone.utc)
    try:
        a = updated_time.objects.get(chart = comp)
        a.update_time = dt
        a.save()
    except:
        data_obj = updated_time(chart = comp, update_time = dt)
        data_obj.save()

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

def insert_data(span, comp, date, data):
    try:
        # print("try block")
        yahoo_obj = yahoo_data.objects.get(chart = comp ,chart_type = span, date = date)    #date already exists
        yahoo_obj.data = data
        yahoo_obj.save()
    except:
        # print("except block")
        yahoo_obj = yahoo_data(chart = comp ,chart_type = span, data = data, date = date)   #date doesn't exist
        yahoo_obj.save()
        yahoo_obj_2 = yahoo_data.objects.filter(chart = comp ,chart_type = span).first()
        if yahoo_obj_2:
            yahoo_obj_2.delete()

# api to push the coal data into the database, that is being pulled on azure functions
@api_view(['POST'])
def push_coal(request):
    try:
        data = request.data["data"]
        date_list = fetch_date()
        print(date_list)
        date_len = len(date_list)
        print(data)
        if date_len!=0:
            date = date_list[0][0]
            insert_data("1week", "MFFH22.NYM", date, data)
            insert_data("1month", "MFFH22.NYM", date, data)
            insert_data("3month", "MFFH22.NYM", date, data)
            insert_data("6month", "MFFH22.NYM", date, data)
            insert_data("1year", "MFFH22.NYM", date, data)
            insert_data("2year", "MFFH22.NYM", date, data)
            print("Coal data pulled")

            coal_obj = stock_data.objects.all().filter(chart_type = "MFFH22.NYM")
            # coal_data = []
            for n in coal_obj:
                pre_val = n.current
            print(pre_val)
            diff = (float(data) - pre_val)
            diff_per = round(((diff/pre_val)*100), 2)
            data = float(data)
            print(diff_per)
            stock_data.objects.filter(chart_type = 'MFFH22.NYM').delete()
            data_obj = stock_data(chart_type = 'MFFH22.NYM' , data = diff_per, current = round(data,2))
            data_obj.save()
            print("Stock chart updated for Coal")
            insert_updated_time('MFFH22.NYM')
    except:
        # print("oops")
        url = "http://localhost:8000/texisle-app/send_mail/"
        payload={'content': 'Issue with daily coal data pull'}
        response = requests.request("POST", url, headers={}, data=payload, files={})
    return Response({"status":200})
    
################################################################
# api no longer used 
@api_view(['GET'])
def coal_data_pull(request):
    try:
        date_list = fetch_date()
        print(date_list)
        date_len = len(date_list)
        if date_len!=0:
            date = date_list[0][0]
            print("Pulling data for ", date)
            url = "https://www.cmegroup.com/CmeWS/mvc/Quotes/Future/5941/G"
            page=urllib.request.Request(url,headers={'User-Agent': 'PostmanRuntime/7.28.4'}) 
            infile=urllib.request.urlopen(page).read()
            data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1
            data = data.replace('<br />','' )
            data1= json.loads(data)
            quotes = data1["quotes"]
            data = float(quotes[0]['priorSettle'])
            # print(data)
            yahoo_obj = yahoo_data(chart = "MFFH22.NYM" ,chart_type = "1week" , data = data, date = date)
            yahoo_obj.save()
            yahoo_obj = yahoo_data(chart = "MFFH22.NYM" ,chart_type = "1month" , data = data, date = date)
            yahoo_obj.save()
            yahoo_obj = yahoo_data(chart = "MFFH22.NYM" ,chart_type = "3month" , data = data, date = date)
            yahoo_obj.save()
            yahoo_obj = yahoo_data(chart = "MFFH22.NYM" ,chart_type = "6month" , data = data, date = date)
            yahoo_obj.save()
            yahoo_obj = yahoo_data(chart = "MFFH22.NYM" ,chart_type = "1year" , data = data, date = date)
            yahoo_obj.save()
            yahoo_obj = yahoo_data(chart = "MFFH22.NYM" ,chart_type = "2year" , data = data, date = date)
            yahoo_obj.save()

            yahoo_obj = yahoo_data.objects.filter(chart = "MFFH22.NYM" ,chart_type = "1week").first()
            yahoo_obj.delete()
            yahoo_obj = yahoo_data.objects.filter(chart = "MFFH22.NYM" ,chart_type = "1month").first()
            yahoo_obj.delete()
            yahoo_obj = yahoo_data.objects.filter(chart = "MFFH22.NYM" ,chart_type = "3month").first()
            yahoo_obj.delete()
            yahoo_obj = yahoo_data.objects.filter(chart = "MFFH22.NYM" ,chart_type = "6month").first()
            yahoo_obj.delete()
            yahoo_obj = yahoo_data.objects.filter(chart = "MFFH22.NYM" ,chart_type = "1year").first()
            yahoo_obj.delete()
            yahoo_obj = yahoo_data.objects.filter(chart = "MFFH22.NYM" ,chart_type = "2year").first()
            yahoo_obj.delete()
            print("Coal data pulled")

            coal_obj = stock_data.objects.all().filter(chart_type = "MFFH22.NYM")
            coal_data = []
            for n in coal_obj:
                pre_val = n.current
            # print(pre_val)
            diff = (float(data) - pre_val)
            diff_per = round(((diff/pre_val)*100), 2)
            # print(diff_per)
            stock_data.objects.filter(chart_type = 'MFFH22.NYM').delete()
            data_obj = stock_data(chart_type = 'MFFH22.NYM' , data = diff_per, current = round(data,2))
            data_obj.save()
            print("Stock chart updated for Coal")
            insert_updated_time('MFFH22.NYM')
    except:
        url = "http://localhost:8000/texisle-app/send_mail/"
        payload={'content': 'Issue with daily coal data pull'}
        response = requests.request("POST", url, headers={}, data=payload, files={})

    return Response({"status":200})
