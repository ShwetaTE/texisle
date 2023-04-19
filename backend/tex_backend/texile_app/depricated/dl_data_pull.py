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
import pyodbc

server = 'texdldwserverprod.database.windows.net'
database = 'tex-dl-dw-prod'
username = 'Marketing_Admin'
password = 'T3x!$l32019'   
driver= '{ODBC Driver 17 for SQL Server}'

@api_view(['GET'])
def dl_daily_data_pull(request):
    # print("started pulling scrap data...")
    scrap()
    # print("started pulling hrc data...")
    hrc()
    # print("started pulling iron data...")
    ironore()
    # print("=================================")
    # print("TURN OFF THE DATA LAKE!!!!!!!!!!")
    # print("=================================")
    return Response({'status': 200})

@api_view(['GET'])
def find_if_works(request):
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT [LastReadDate], [MBIOIndexIronOreCFRChinaIndex] FROM [dbo].[KPI_Indicator_Spot_Price] where LastReadDate>= DATEADD(day, -4, GetDate()) order by year(LastReadDate),month(LastReadDate),day(LastReadDate);")
            data_list = []
            for each in cursor:
                data_list.append(each)
    print(data_list)
    data = data_list[0]
    val = data[1]
    dt = datetime.strptime(data[0], '%m/%d/%Y %H:%M:%S %p')
    date = dt.strftime('%m/%d/%Y')
    print(date + " " + val)
    return Response({'data':val,'date':date})

def scrap():
    try:
        day = datetime.today().weekday()
        if day == 0:
            with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT [LastReadDate], [NYMEXMidwwestNo.1BushelingScrap] FROM [dbo].[KPI_Indicator_Spot_Price] where LastReadDate>= DATEADD(day, -4, GetDate()) order by year(LastReadDate),month(LastReadDate),day(LastReadDate);")
                    data_list = []
                    for each in cursor:
                        data_list.append(each)
        else:
            with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT [LastReadDate], [NYMEXMidwwestNo.1BushelingScrap] FROM [dbo].[KPI_Indicator_Spot_Price] where LastReadDate>= DATEADD(day, -2, GetDate()) order by year(LastReadDate),month(LastReadDate),day(LastReadDate);")
                    data_list = []
                    for each in cursor:
                        data_list.append(each)
        data = data_list[0]
        val = data[1]
        dt = datetime.strptime(data[0], '%m/%d/%Y %H:%M:%S %p')
        date = dt.strftime('%m/%d/%Y')
        # print(date + " " + val)

        try:
            data_obj = Scrap_data.objects.get(chart_type = "1week", date = date)    #date already exists
            data_obj.data = val
            data_obj.save()
            data_obj = Scrap_data.objects.get(chart_type = "1month", date = date)    #date already exists
            data_obj.data = val
            data_obj.save()
            data_obj = Scrap_data.objects.get(chart_type = "3month", date = date)    #date already exists
            data_obj.data = val
            data_obj.save()
            data_obj = Scrap_data.objects.get(chart_type = "6month", date = date)    #date already exists
            data_obj.data = val
            data_obj.save()
            data_obj = Scrap_data.objects.get(chart_type = "1year", date = date)    #date already exists
            data_obj.data = val
            data_obj.save()
            data_obj = Scrap_data.objects.get(chart_type = "2year", date = date)    #date already exists
            data_obj.data = val
            data_obj.save()
            
        except:
            scrap_obj = Scrap_data(chart_type = "1week" , data = val, date = date)
            scrap_obj.save()
            scrap_obj = Scrap_data(chart_type = "1month" , data = val, date = date)
            scrap_obj.save()
            scrap_obj = Scrap_data(chart_type = "3month" , data = val, date = date)
            scrap_obj.save()
            scrap_obj = Scrap_data(chart_type = "6month" , data = val, date = date)
            scrap_obj.save()
            scrap_obj = Scrap_data(chart_type = "1year" , data = val, date = date)
            scrap_obj.save()
            scrap_obj = Scrap_data(chart_type = "2year" , data = val, date = date)
            scrap_obj.save()

            scrap_obj = Scrap_data.objects.filter(chart_type = "1week").first()
            scrap_obj.delete()
            scrap_obj = Scrap_data.objects.filter(chart_type = "1month").first()
            scrap_obj.delete()
            scrap_obj = Scrap_data.objects.filter(chart_type = "3month").first()
            scrap_obj.delete()
            scrap_obj = Scrap_data.objects.filter(chart_type = "6month").first()
            scrap_obj.delete()
            scrap_obj = Scrap_data.objects.filter(chart_type = "1year").first()
            scrap_obj.delete()
            scrap_obj = Scrap_data.objects.filter(chart_type = "2year").first()
            scrap_obj.delete()

            stock_diff('scrap', val)
            insert_updated_time('scrap')
    except:
        url = "http://localhost:8000/texisle-app/send_mail/"
        payload={'content': 'Issue with daily scrap data pull'}
        response = requests.request("POST", url, headers={}, data=payload, files={})
    return()

def hrc():
    try:
        day = datetime.today().weekday()
        if day == 0:
            with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT [LastReadDate], [HRCDomesticFOBMidwestMill] FROM [dbo].[KPI_Indicator_Spot_Price] where LastReadDate>= DATEADD(day, -4, GetDate()) order by year(LastReadDate),month(LastReadDate),day(LastReadDate);")
                    data_list = []
                    for each in cursor:
                        data_list.append(each)
        else:
            with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT [LastReadDate], [HRCDomesticFOBMidwestMill] FROM [dbo].[KPI_Indicator_Spot_Price] where LastReadDate>= DATEADD(day, -2, GetDate()) order by year(LastReadDate),month(LastReadDate),day(LastReadDate);")
                    data_list = []
                    for each in cursor:
                        data_list.append(each)
        # print(data_list)
        data = data_list[0]
        val = data[1]
        dt = datetime.strptime(data[0], '%m/%d/%Y %H:%M:%S %p')
        date = dt.strftime('%m/%d/%Y')

        try:
            data_obj = HRC_data.objects.get(chart_type = "1week", date = date)    #date already exists
            data_obj.data = val
            data_obj.save()
            data_obj = HRC_data.objects.get(chart_type = "1month", date = date)    #date already exists
            data_obj.data = val
            data_obj.save()
            data_obj = HRC_data.objects.get(chart_type = "3month", date = date)    #date already exists
            data_obj.data = val
            data_obj.save()
            data_obj = HRC_data.objects.get(chart_type = "6month", date = date)    #date already exists
            data_obj.data = val
            data_obj.save()
            data_obj = HRC_data.objects.get(chart_type = "1year", date = date)    #date already exists
            data_obj.data = val
            data_obj.save()
            data_obj = HRC_data.objects.get(chart_type = "2year", date = date)    #date already exists
            data_obj.data = val
            data_obj.save()
        except:
            hrc_obj = HRC_data(chart_type = "1week" , data = val, date = date)
            hrc_obj.save()
            hrc_obj = HRC_data(chart_type = "1month" , data = val, date = date)
            hrc_obj.save()
            hrc_obj = HRC_data(chart_type = "3month" , data = val, date = date)
            hrc_obj.save()
            hrc_obj = HRC_data(chart_type = "6month" , data = val, date = date)
            hrc_obj.save()
            hrc_obj = HRC_data(chart_type = "1year" , data = val, date = date)
            hrc_obj.save()
            hrc_obj = HRC_data(chart_type = "2year" , data = val, date = date)
            hrc_obj.save()

            hrc_obj = HRC_data.objects.filter(chart_type = "1week").first()
            hrc_obj.delete()
            hrc_obj = HRC_data.objects.filter(chart_type = "1month").first()
            hrc_obj.delete()
            hrc_obj = HRC_data.objects.filter(chart_type = "3month").first()
            hrc_obj.delete()
            hrc_obj = HRC_data.objects.filter(chart_type = "6month").first()
            hrc_obj.delete()
            hrc_obj = HRC_data.objects.filter(chart_type = "1year").first()
            hrc_obj.delete()
            hrc_obj = HRC_data.objects.filter(chart_type = "2year").first()
            hrc_obj.delete()

            stock_diff('hrc', val)
            insert_updated_time('hrc')
    except:
        url = "http://localhost:8000/texisle-app/send_mail/"
        payload={'content': 'Issue with daily HRC data pull'}
        response = requests.request("POST", url, headers={}, data=payload, files={})
    return()

def ironore():
    try:
        day = datetime.today().weekday()
        if day == 0:
            with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT [LastReadDate], [MBIOIndexIronOreCFRChinaIndex] FROM [dbo].[KPI_Indicator_Spot_Price] where LastReadDate>= DATEADD(day, -4, GetDate()) order by year(LastReadDate),month(LastReadDate),day(LastReadDate);")
                    data_list = []
                    for each in cursor:
                        data_list.append(each)
        else:
            with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT [LastReadDate], [MBIOIndexIronOreCFRChinaIndex] FROM [dbo].[KPI_Indicator_Spot_Price] where LastReadDate>= DATEADD(day, -2, GetDate()) order by year(LastReadDate),month(LastReadDate),day(LastReadDate);")
                    data_list = []
                    for each in cursor:
                        data_list.append(each)
        # print(data_list)
        data = data_list[0]
        val = data[1]
        dt = datetime.strptime(data[0], '%m/%d/%Y %H:%M:%S %p')
        date = dt.strftime('%m/%d/%Y')

        try:
            data_obj = iron_data.objects.get(chart_type = "1week", date = date)    #date already exists
            data_obj.data = val
            data_obj.save()
            data_obj = iron_data.objects.get(chart_type = "1month", date = date)    #date already exists
            data_obj.data = val
            data_obj.save()
            data_obj = iron_data.objects.get(chart_type = "3month", date = date)    #date already exists
            data_obj.data = val
            data_obj.save()
            data_obj = iron_data.objects.get(chart_type = "6month", date = date)    #date already exists
            data_obj.data = val
            data_obj.save()
            data_obj = iron_data.objects.get(chart_type = "1year", date = date)    #date already exists
            data_obj.data = val
            data_obj.save()
            data_obj = iron_data.objects.get(chart_type = "2year", date = date)    #date already exists
            data_obj.data = val
            data_obj.save()
        except:
            iron_obj = iron_data(chart_type = "1week" , data = val, date = date)
            iron_obj.save()
            iron_obj = iron_data(chart_type = "1month" , data = val, date = date)
            iron_obj.save()
            iron_obj = iron_data(chart_type = "3month" , data = val, date = date)
            iron_obj.save()
            iron_obj = iron_data(chart_type = "6month" , data = val, date = date)
            iron_obj.save()
            iron_obj = iron_data(chart_type = "1year" , data = val, date = date)
            iron_obj.save()
            iron_obj = iron_data(chart_type = "2year" , data = val, date = date)
            iron_obj.save()

            iron_obj = iron_data.objects.filter(chart_type = "1week").first()
            iron_obj.delete()
            iron_obj = iron_data.objects.filter(chart_type = "1month").first()
            iron_obj.delete()
            iron_obj = iron_data.objects.filter(chart_type = "3month").first()
            iron_obj.delete()
            iron_obj = iron_data.objects.filter(chart_type = "6month").first()
            iron_obj.delete()
            iron_obj = iron_data.objects.filter(chart_type = "1year").first()
            iron_obj.delete()
            iron_obj = iron_data.objects.filter(chart_type = "2year").first()
            iron_obj.delete()

            stock_diff('iron', val)
            insert_updated_time('iron')
    except:
        url = "http://localhost:8000/texisle-app/send_mail/"
        payload={'content': 'Issue with daily IronOre data pull'}
        response = requests.request("POST", url, headers={}, data=payload, files={})
    return()

def stock_diff(chart, data):
    data_obj = stock_data.objects.all().filter(chart_type = chart)
    for n in data_obj:
        pre_val = n.current
    data = float(data)
    # print(pre_val)
    diff = (data - pre_val)
    diff_per = round(((diff/pre_val)*100), 2)
    # print(diff_per)
    stock_data.objects.filter(chart_type = chart).delete()
    data_obj = stock_data(chart_type = chart , data = diff_per, current = round(data,2))
    data_obj.save()
    # print("Stock chart updated for "+chart)

def insert_updated_time(comp):
    dt = datetime.now(tz=timezone.utc)
    try:
        a = updated_time.objects.get(chart = comp)
        a.update_time = dt
        a.save()
    except:
        data_obj = updated_time(chart = comp, update_time = dt)
        data_obj.save()