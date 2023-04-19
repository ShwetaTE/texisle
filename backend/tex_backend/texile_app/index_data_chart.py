from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from newspaper.extractors import RE_LANG
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
from django_pandas.io import read_frame
from numpy import ERR_CALL
import pandas_market_calendars as mcal
from datetime import datetime, timedelta, date
import yfinance as yf
import pandas as pd
import numpy as np
import time, os
from datetime import datetime
from datetime import datetime, timedelta, date

# API's to fetch data from table to show on charts
@api_view(['POST'])
def index_data_1(request):
    chart = request.data["chart"]
    data_df = data_object_select(chart)
    # print(data_df)
    data = data_df.values.tolist()
    temp = latest_data(chart)
    if temp != []:
        # print(data)
        # print(temp)
        data.append(temp)
    data = data[-5:]

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

@api_view(['POST'])
def index_data_2(request):
    chart = request.data["chart"]
    data_df = data_object_select(chart)
    data = data_df.values.tolist()
    temp = latest_data(chart)
    if temp != []:
        # print(data)
        # print(temp)
        data.append(temp)
    data = data[-22:]

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

@api_view(['POST'])
def index_data_3(request):
    chart = request.data["chart"]
    data_df = data_object_select(chart)
    data = data_df.values.tolist()
    temp = latest_data(chart)
    if temp != []:
        # print(data)
        # print(temp)
        data.append(temp)
    data = data[-66:]

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

@api_view(['POST'])
def index_data_4(request):
    chart = request.data["chart"]
    data_df = data_object_select(chart)
    data = data_df.values.tolist()
    temp = latest_data(chart)
    if temp != []:
        # print(data)
        # print(temp)
        data.append(temp)
    data = data[-132:]

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

@api_view(['POST'])
def index_data_5(request):
    chart = request.data["chart"]
    data_df = data_object_select(chart)
    data = data_df.values.tolist()
    temp = latest_data(chart)
    if temp != []:
        # print(data)
        # print(temp)
        data.append(temp)
    data = data[-264:]

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

@api_view(['POST'])
def index_data_6(request):
    chart = request.data["chart"]
    data_df = data_object_select(chart)
    data = data_df.values.tolist()
    temp = latest_data(chart)
    if temp != []:
        # print(data)
        # print(temp)
        data.append(temp)
    data = data[-507:]
    
    # print(data)
    
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

def data_object_select(chart):
    if chart == "raw material index":
        # index_obj = index_rmi_data.objects.all()
        index_obj = index_rmi_cme_data.objects.all()
        data_df = read_frame(index_obj, fieldnames=['date','RMI_index'])
    if chart == "pipe manufacturing":
        index_obj = index_pmf_data.objects.all()
        data_df = read_frame(index_obj, fieldnames=['date','PMF_index'])
    if chart == "steel manufacturing":
        index_obj = index_smf_data.objects.all()
        data_df = read_frame(index_obj, fieldnames=['date','SMF_index'])
    if chart == "iron ore mining":
        index_obj = index_iom_data.objects.all()
        data_df = read_frame(index_obj, fieldnames=['date','IOM_index'])
    if chart == "fuel":
        index_obj = index_f_data.objects.all()
        data_df = read_frame(index_obj, fieldnames=['date','F_index'])
    if chart == "transport":
        index_obj = index_t_data.objects.all()
        data_df = read_frame(index_obj, fieldnames=['date','T_index'])
    if chart == "rig index":
        index_obj = index_rig_data.objects.all()
        data_df = read_frame(index_obj, fieldnames=['date','RC_index'])
    return(data_df)

def latest_data(chart):
    try:
        data_obj = daily_index.objects.filter(chart = chart)
        for each in data_obj:
            # print(each)
            data = each.val
            date = each.date
        val = [date, data]
    except:
        val = []
    # print(date +" "+ data)
    return(val)
