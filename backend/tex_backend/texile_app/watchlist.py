from tabnanny import check
from turtle import Terminator
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from newspaper.extractors import RE_LANG
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
from django_pandas.io import read_frame
from django.utils import timezone
import requests
import time, os
from datetime import datetime

# add tickers to watchlist config table
@api_view(['POST'])
def add_watchlist(request):
    chart_list = request.data["chart_list"]
    deviceID = request.data['deviceID']
    app = request.data['app_type']
    list1 = chart_list
    str1 = ' '.join(list1)
    print(str1)
    try:
        a = watchlist.objects.get(deviceID = deviceID, app = app)
        a.config = str1
        a.save()
    except:
        dt = datetime.now(tz=timezone.utc)
        data_obj = watchlist(app = app, deviceID = deviceID, created_time = dt, config = str1)
        data_obj.save()
    return Response({"status":200})

# add tickers to watchlist config table
@api_view(['POST'])
def update_watchlist(request):
    chart = request.data["chart"]
    deviceID = request.data['deviceID']
    app = request.data['app_type']
    try:
        a = watchlist.objects.all().filter(app = app, deviceID = deviceID)[0]
        str = a.config
        print(str)
        if str == "":
            chart_list = []
        else:
            chart_list = list(str.split(" "))
        print(chart_list)
        check = chart_list.count(chart)
        if check == 0:
            chart_list.append(chart)
            str1 = ' '.join(chart_list)
            a = watchlist.objects.get(deviceID = deviceID, app = app)
            a.config = str1
            a.save()
        if check == 1:
            chart_list.remove(chart)
            str1 = ' '.join(chart_list)
            a = watchlist.objects.get(deviceID = deviceID, app = app)
            a.config = str1
            a.save()
    except:
        dt = datetime.now(tz=timezone.utc)
        data_obj = watchlist(app = app, deviceID = deviceID, created_time = dt, config = chart)
        data_obj.save()
    return Response({"status":200})
    
# fetch watchlist config for device
@api_view(['POST'])
def watchlist_config(request):
    deviceID = request.data['deviceID']
    app = request.data['app_type']
    try:
        a = watchlist.objects.all().filter(app = app, deviceID = deviceID)[0]
        str = a.config
        if str == "":
            chart_list = []
        else:
            chart_list = list(str.split(" "))
        return Response({"chart_list":chart_list, "exist":1})
    except:
        dt = datetime.now(tz=timezone.utc)
        data_obj = watchlist(app = app, deviceID = deviceID, created_time = dt)
        data_obj.save()
        return Response({"chart_list":[], "exist":0})
    # return Response({"status":200})