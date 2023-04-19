from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from joblib import PrintTime
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

def insert_data(comp, date, data):
    try:
        # print("try block")
        yahoo_obj = rmi_data.objects.get(chart = comp, date = date)    #date already exists
        yahoo_obj.data = data
        yahoo_obj.save()
    except:
        # print("except block")
        yahoo_obj = rmi_data(chart = comp , data = data, date = date)   #date doesn't exist
        yahoo_obj.save()


# stores daily rmi tickers data
@api_view(['POST'])
def rmi_cme_data_push(request):
    try:
        chart = request.data["chart"]
        data = request.data["data"]
        print(chart, data)
        date_list = fetch_date()
        # print("date--> ",date_list)
        date_len = len(date_list)
        # print("data--> ",data)
        if date_len!=0:
            date = date_list[0][0]
            insert_data(chart, date, data)
            # print(chart +" data pulled")
            if chart == "Iron":
                chart = 'iron'
            if chart == "Scrap":
                chart = 'scrap'
            if chart == "HRC":
                chart = 'hrc'
            coal_obj = stock_data.objects.all().filter(chart_type = chart)
            # coal_data = []
            for n in coal_obj:
                pre_val = n.current
            # print("pre_val---> ",pre_val)
            diff = (float(data) - pre_val)
            diff_per = round(((diff/pre_val)*100), 2)
            data = float(data)
            # print("diff---> ",diff_per)
            stock_data.objects.filter(chart_type = chart).delete()
            data_obj = stock_data(chart_type = chart , data = diff_per, current = round(data,2))
            data_obj.save()
            print("Stock chart updated for "+ chart)
            insert_updated_time(chart) 
    except:
        print("failed")
        # url = "http://localhost:8000/texisle-app/send_mail/"
        # payload={'content': 'Issue with daily '+chart+' data pull'}
        # response = requests.request("POST", url, headers={}, data=payload, files={})
    return Response({"status":200})