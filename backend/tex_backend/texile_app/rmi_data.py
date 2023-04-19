from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
import json
from django.core import serializers
import time, os
from datetime import datetime
import requests

# fetch data for rmi tickers to display on charts
@api_view(['POST'])
def rmi_chart_data(request):
    chart = request.data["chart"]
    frequency = request.data["frequency"]
    if chart == "Scrap":
        data = Scrap_fetch(frequency)
    if chart == "HRC":
        data = HRC_fetch(frequency)
    if chart == "Iron":
        data = Iron_fetch(frequency)
    return Response(data)

def Scrap_fetch(freq):
    data_obj = rmi_data.objects.filter(chart = "Scrap")
    f_val = []
    val = []
    for each in data_obj:
        data = each.data
        date = each.date
        temp = [date, data]
        val.append(temp)
    final_data = []
    if freq == "1week":
        f_val = val[-8:]
        hist_data = convert_date_to_epoch(f_val)
        data = f_data("Scrap")
        # print(data)
        temp_future_data = data[:9]
        temp_data = data[0][1]
        initial_val = [hist_data[-1]]
        initial_val[0][1]=temp_data
        future_data = initial_val + temp_future_data
        final_data = [hist_data, future_data]
    if freq == "1month":
        f_val = val[-22:]
        hist_data = convert_date_to_epoch(f_val)
        data = f_data("Scrap")
        # print(data)
        temp_future_data = data[:9]
        temp_data = data[0][1]
        initial_val = [hist_data[-1]]
        initial_val[0][1]=temp_data
        future_data = initial_val + temp_future_data
        final_data = [hist_data, future_data]
    if freq == "3month":
        f_val = val[-66:]
        hist_data = convert_date_to_epoch(f_val)
        data = f_data("Scrap")
        # print(data)
        temp_future_data = data[:11]
        temp_data = data[0][1]
        initial_val = [hist_data[-1]]
        initial_val[0][1]=temp_data
        future_data = initial_val + temp_future_data
        final_data = [hist_data, future_data]
    if freq == "6month":
        f_val = val[-132:]
        hist_data = convert_date_to_epoch(f_val)
        data = f_data("Scrap")
        # print(data)
        temp_future_data = data[:12]
        temp_data = data[0][1]
        initial_val = [hist_data[-1]]
        initial_val[0][1]=temp_data
        future_data = initial_val + temp_future_data
        final_data = [hist_data, future_data]
    if freq == "1year":
        f_val = val[-264:]
        hist_data = convert_date_to_epoch(f_val)
        data = f_data("Scrap")
        # print(data)
        temp_future_data = data[:18]
        temp_data = data[0][1]
        initial_val = [hist_data[-1]]
        initial_val[0][1]=temp_data
        future_data = initial_val + temp_future_data
        final_data = [hist_data, future_data]
    if freq == "2year":
        f_val = val[-528:]
        hist_data = convert_date_to_epoch(f_val)
        data = f_data("Scrap")
        temp_future_data= data
        temp = [hist_data[-1]]
        future_data = temp + temp_future_data
        final_data = [hist_data, future_data]
    return(final_data)

def HRC_fetch(freq):
    data_obj = rmi_data.objects.filter(chart = "HRC")
    f_val = []
    val = []
    for each in data_obj:
        data = each.data
        date = each.date
        temp = [date, data]
        val.append(temp)
    final_data = []
    if freq == "1week":
        f_val = val[-6:]
        hist_data = convert_date_to_epoch(f_val)
        data = f_data("HRC")
        # print(data)
        temp_future_data = data[:9]
        temp_data = data[0][1]
        initial_val = [hist_data[-1]]
        initial_val[0][1]=temp_data
        future_data = initial_val + temp_future_data
        final_data = [hist_data, future_data]
    if freq == "1month":
        f_val = val[-22:]
        hist_data = convert_date_to_epoch(f_val)
        data = f_data("HRC")
        # print(data)
        temp_future_data = data[:9]
        temp_data = data[0][1]
        initial_val = [hist_data[-1]]
        initial_val[0][1]=temp_data
        future_data = initial_val + temp_future_data
        final_data = [hist_data, future_data]
    if freq == "3month":
        f_val = val[-66:]
        hist_data = convert_date_to_epoch(f_val)
        data = f_data("HRC")
        # print(data)
        temp_future_data = data[:11]
        temp_data = data[0][1]
        initial_val = [hist_data[-1]]
        initial_val[0][1]=temp_data
        future_data = initial_val + temp_future_data
        final_data = [hist_data, future_data]
    if freq == "6month":
        f_val = val[-132:]
        hist_data = convert_date_to_epoch(f_val)
        data = f_data("HRC")
        # print(data)
        temp_future_data = data[:13]
        temp_data = data[0][1]
        initial_val = [hist_data[-1]]
        initial_val[0][1]=temp_data
        future_data = initial_val + temp_future_data
        final_data = [hist_data, future_data]
    if freq == "1year":
        f_val = val[-264:]
        hist_data = convert_date_to_epoch(f_val)
        data = f_data("HRC")
        # print(data)
        temp_future_data = data[:19]
        temp_data = data[0][1]
        initial_val = [hist_data[-1]]
        initial_val[0][1]=temp_data
        future_data = initial_val + temp_future_data
        final_data = [hist_data, future_data]
    if freq == "2year":
        f_val = val[-528:]
        hist_data = convert_date_to_epoch(f_val)
        data = f_data("HRC")
        temp_future_data= data
        temp = [hist_data[-1]]
        future_data = temp + temp_future_data
        final_data = [hist_data, future_data]
    return(final_data)

def Iron_fetch(freq):
    data_obj = rmi_data.objects.filter(chart = "Iron")
    f_val = []
    val = []
    for each in data_obj:
        data = each.data
        date = each.date
        temp = [date, data]
        val.append(temp)
    final_data = []
    if freq == "1week":
        f_val = val[-6:]
        hist_data = convert_date_to_epoch(f_val)
        data = f_data("iron")
        # print(data)
        temp_future_data = data[:7]
        temp_data = data[0][1]
        initial_val = [hist_data[-1]]
        initial_val[0][1]=temp_data
        future_data = initial_val + temp_future_data
        final_data = [hist_data, future_data]
    if freq == "1month":
        f_val = val[-22:]
        hist_data = convert_date_to_epoch(f_val)
        data = f_data("iron")
        # print(data)
        temp_future_data = data[:8]
        temp_data = data[0][1]
        initial_val = [hist_data[-1]]
        initial_val[0][1]=temp_data
        future_data = initial_val + temp_future_data
        final_data = [hist_data, future_data]
    if freq == "3month":
        f_val = val[-66:]
        hist_data = convert_date_to_epoch(f_val)
        data = f_data("iron")
        # print(data)
        temp_future_data = data[:9]
        temp_data = data[0][1]
        initial_val = [hist_data[-1]]
        initial_val[0][1]=temp_data
        future_data = initial_val + temp_future_data
        final_data = [hist_data, future_data]
    if freq == "6month":
        f_val = val[-132:]
        hist_data = convert_date_to_epoch(f_val)
        data = f_data("iron")
        # print(data)
        temp_future_data = data[:13]
        temp_data = data[0][1]
        initial_val = [hist_data[-1]]
        initial_val[0][1]=temp_data
        future_data = initial_val + temp_future_data
        final_data = [hist_data, future_data]
    if freq == "1year":
        f_val = val[-264:]
        hist_data = convert_date_to_epoch(f_val)
        data = f_data("iron")
        # print(data)
        temp_future_data = data[:19]
        temp_data = data[0][1]
        initial_val = [hist_data[-1]]
        initial_val[0][1]=temp_data
        future_data = initial_val + temp_future_data
        final_data = [hist_data, future_data]
    if freq == "2year":
        f_val = val[-528:]
        hist_data = convert_date_to_epoch(f_val)
        data = f_data("iron")
        temp_future_data= data
        temp = [hist_data[-1]]
        future_data = temp + temp_future_data
        final_data = [hist_data, future_data]
    return(final_data)


def multiplier(data, mult):
    for each in data:
        each[1] = each[1]*mult
    return(data)

def f_data(chart):
    yahoo_obj = future_yahoo_data.objects.all().filter(chart = chart)
    data = []
    for n in yahoo_obj:
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
    
    return(final_data)

def convert_date_to_epoch(data):
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
    return(final_data)