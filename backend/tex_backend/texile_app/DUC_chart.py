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

@api_view(['POST'])
def duc_data_1(request):
    final_data = []

    return Response(final_data)

@api_view(['POST'])
def duc_data_2(request):
    final_data = []
    chart = request.data["chart"]
    chart_list = [chart+"_D", chart+"_C", chart+"_DUC"]
    for each in chart_list:
        data_df = data_object_select(each)
        # print(data_df)
        data = data_df.values.tolist()
        temp = latest_data(each)
        if temp != []:
            data.append(temp)
        data = data[-2:]
        
        date = []
        temp_data = []
        for i in data:
            i[0] = i[0].replace("/","-")
            date.append(i[0])

        date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
        temp_data = []
        for i in date:
            for j in data:
                if j[0] == i:
                    tmp = []
                    tmp.append(i)
                    tmp.append(j[1])
                    temp_data.append(tmp)
                    break

        for i in temp_data:
            date = i[0] #+ " 00:00:00"
            pattern = '%m-%d-%Y' # %H:%M:%S'
            epoch = int(time.mktime(time.strptime(date, pattern)))
            i[0] = epoch*1000
            if i[1]!=None:
                i[1] = float(i[1])
        final_data.append(temp_data)
        # print(temp_data)

    return Response(final_data)

@api_view(['POST'])
def duc_data_3(request):
    final_data = []
    chart = request.data["chart"]
    chart_list = [chart+"_D", chart+"_C", chart+"_DUC"]
    for each in chart_list:
        data_df = data_object_select(each)
        # print(data_df)
        data = data_df.values.tolist()
        temp = latest_data(each)
        if temp != []:
            data.append(temp)
        data = data[-3:]
        
        date = []
        temp_data = []
        for i in data:
            i[0] = i[0].replace("/","-")
            date.append(i[0])

        date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
        temp_data = []
        for i in date:
            for j in data:
                if j[0] == i:
                    tmp = []
                    tmp.append(i)
                    tmp.append(j[1])
                    temp_data.append(tmp)
                    break

        for i in temp_data:
            date = i[0] #+ " 00:00:00"
            pattern = '%m-%d-%Y' # %H:%M:%S'
            epoch = int(time.mktime(time.strptime(date, pattern)))
            i[0] = epoch*1000
            if i[1]!=None:
                i[1] = float(i[1])
        final_data.append(temp_data)
        # print(temp_data)

    return Response(final_data)

@api_view(['POST'])
def duc_data_4(request):
    final_data = []
    chart = request.data["chart"]
    chart_list = [chart+"_D", chart+"_C", chart+"_DUC"]
    for each in chart_list:
        data_df = data_object_select(each)
        # print(data_df)
        data = data_df.values.tolist()
        temp = latest_data(each)
        if temp != []:
            data.append(temp)
        data = data[-6:]
        
        date = []
        temp_data = []
        for i in data:
            i[0] = i[0].replace("/","-")
            date.append(i[0])

        date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
        temp_data = []
        for i in date:
            for j in data:
                if j[0] == i:
                    tmp = []
                    tmp.append(i)
                    tmp.append(j[1])
                    temp_data.append(tmp)
                    break

        for i in temp_data:
            date = i[0] #+ " 00:00:00"
            pattern = '%m-%d-%Y' # %H:%M:%S'
            epoch = int(time.mktime(time.strptime(date, pattern)))
            i[0] = epoch*1000
            if i[1]!=None:
                i[1] = float(i[1])
        final_data.append(temp_data)
        # print(temp_data)

    return Response(final_data)

@api_view(['POST'])
def duc_data_5(request):
    final_data = []
    chart = request.data["chart"]
    chart_list = [chart+"_D", chart+"_C", chart+"_DUC"]
    for each in chart_list:
        data_df = data_object_select(each)
        # print(data_df)
        data = data_df.values.tolist()
        temp = latest_data(each)
        if temp != []:
            data.append(temp)
        data = data[-12:]
        
        date = []
        temp_data = []
        for i in data:
            i[0] = i[0].replace("/","-")
            date.append(i[0])

        date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
        temp_data = []
        for i in date:
            for j in data:
                if j[0] == i:
                    tmp = []
                    tmp.append(i)
                    tmp.append(j[1])
                    temp_data.append(tmp)
                    break

        for i in temp_data:
            date = i[0] #+ " 00:00:00"
            pattern = '%m-%d-%Y' # %H:%M:%S'
            epoch = int(time.mktime(time.strptime(date, pattern)))
            i[0] = epoch*1000
            if i[1]!=None:
                i[1] = float(i[1])
        final_data.append(temp_data)
        # print(temp_data)

    return Response(final_data)

@api_view(['POST'])
def duc_data_6(request):
    final_data = []
    chart = request.data["chart"]
    chart_list = [chart+"_D", chart+"_C", chart+"_DUC"]
    for each in chart_list:
        data_df = data_object_select(each)
        # print(data_df)
        data = data_df.values.tolist()
        temp = latest_data(each)
        if temp != []:
            data.append(temp)
        data = data[-24:]
        
        date = []
        temp_data = []
        for i in data:
            i[0] = i[0].replace("/","-")
            date.append(i[0])

        date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
        temp_data = []
        for i in date:
            for j in data:
                if j[0] == i:
                    tmp = []
                    tmp.append(i)
                    tmp.append(j[1])
                    temp_data.append(tmp)
                    break

        for i in temp_data:
            date = i[0] #+ " 00:00:00"
            pattern = '%m-%d-%Y' # %H:%M:%S'
            epoch = int(time.mktime(time.strptime(date, pattern)))
            i[0] = epoch*1000
            if i[1]!=None:
                i[1] = float(i[1])
        final_data.append(temp_data)
        # print(temp_data)

    return Response(final_data)

def data_object_select(chart):
    # if chart == "Anadarko":
    index_obj = index_duc_data.objects.all()
    data_df = read_frame(index_obj, fieldnames=['date',chart])
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
