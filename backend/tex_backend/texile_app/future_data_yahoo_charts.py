from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
from typing import final
import requests
from bs4 import BeautifulSoup
import urllib.parse
from datetime import datetime, timedelta, date
import time, os
from datetime import datetime

# API's to fetch data from table to show on charts
@api_view(['POST'])
def f_y_data_1(request):
    # print(request)
    chart = request.data["chart"]
    # print(chart)
    hist_data = data_1(chart)
    data = f_data(chart)
    # print(data)
    temp_future_data = data[:7]
    temp_data = data[0][1]
    initial_val = [hist_data[-1]]
    initial_val[0][1]=temp_data
    future_data = initial_val + temp_future_data
    return Response([hist_data, future_data])

@api_view(['POST'])
def f_y_data_2(request):
    # print(request)
    chart = request.data["chart"]
    # print(chart)
    hist_data = data_2(chart)
    data = f_data(chart)
    temp_future_data= data[:8]
    temp = [hist_data[-1]]
    future_data = temp + temp_future_data
    return Response([hist_data, future_data])

@api_view(['POST'])
def f_y_data_3(request):
    # print(request)
    chart = request.data["chart"]
    # print(chart)
    hist_data = data_3(chart)
    data = f_data(chart)
    temp_future_data= data[:9]
    temp = [hist_data[-1]]
    future_data = temp + temp_future_data
    return Response([hist_data, future_data])

@api_view(['POST'])
def f_y_data_4(request):
    # print(request)
    chart = request.data["chart"]
    # print(chart)
    hist_data = data_4(chart)
    data = f_data(chart)
    temp_future_data= data[:13]
    temp = [hist_data[-1]]
    future_data = temp + temp_future_data
    return Response([hist_data, future_data])

@api_view(['POST'])
def f_y_data_5(request):
    # print(request)
    chart = request.data["chart"]
    # print(chart)
    hist_data = data_5(chart)
    data = f_data(chart)
    temp_future_data= data[:19]
    temp = [hist_data[-1]]
    future_data = temp + temp_future_data
    return Response([hist_data, future_data])

@api_view(['POST'])
def f_y_data_6(request):
    # print(request)
    chart = request.data["chart"]
    # print(chart)
    hist_data = data_6(chart)
    data = f_data(chart)
    temp_future_data= data
    temp = [hist_data[-1]]
    future_data = temp + temp_future_data
    return Response([hist_data, future_data])

# functions to fetch historical data
def data_1(chart):
    # chart = request.data["chart"]
    yahoo_obj = yahoo_data.objects.all().filter(chart = chart , chart_type = "1week")
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


def data_2(chart):
    # chart = request.data["chart"]
    yahoo_obj = yahoo_data.objects.all().filter(chart = chart , chart_type = "1month")
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


def data_3(chart):
    # chart = request.data["chart"]
    yahoo_obj = yahoo_data.objects.all().filter(chart = chart , chart_type = "3month")
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


def data_4(chart):
    # chart = request.data["chart"]
    yahoo_obj = yahoo_data.objects.all().filter(chart = chart , chart_type = "6month")
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


def data_5(chart):
    # chart = request.data["chart"]
    yahoo_obj = yahoo_data.objects.all().filter(chart = chart , chart_type = "1year")
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


def data_6(chart):
    # chart = request.data["chart"]
    yahoo_obj = yahoo_data.objects.all().filter(chart = chart , chart_type = "2year")
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

# function to fetch the future data
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
