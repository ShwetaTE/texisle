from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
from django.utils import timezone
import json
from django.core import serializers
import time, os
from datetime import datetime
import requests
import yfinance as yf
# from currency_converter import CurrencyConverter
# c = CurrencyConverter()
# from forex_python.converter import CurrencyRates
# c = CurrencyRates()
from py_currency_converter import convert
@csrf_exempt
@api_view(['GET'])
def y_ts_hourly_pull(request):
    print("start pulling data for", 'TS')
    #1 week
    y_data_ts.objects.filter().delete()
    co_obj = yf.Ticker('TS')
    list_date = []
    list_data = []
    list_time=[]
    final_data = []
    hist = co_obj.history(interval="1h")
    # print(hist.index.array)
    date=hist.index.array
    # print(date)
    data = hist["Close"]
    for i in range(len(date)):
        # print(data[i],date[i])
        date_final = datetime.strptime(str(date[i]), "%Y-%m-%d %H:%M:%S-%V:%W").strftime("%Y-%m-%d")
        time_final = datetime.strptime(str(date[i]), "%Y-%m-%d %H:%M:%S-%V:%W").strftime("%Y-%m-%d %H:%M:%S")
        # print(time_final)
        list_date.append(date_final)
        # print(list_date)
        list_time.append(time_final)
        list_data.append(round(data[i],2))
    # print(date,final_data)
    l = len(list_data)
    for i in range(0,l):
      temp_list = [list_date[i],list_data[i],list_time[i]]
      final_data.append(temp_list)
    print("final data",final_data)
    for n in final_data:
        # print(n[1])
       y_data = y_data_ts(chart_type = '1week' , data = n[1], date = n[0],time=n[2])
       y_data.save()
    # print(final_data)
    print("1 week done")
    return Response({"status":200})