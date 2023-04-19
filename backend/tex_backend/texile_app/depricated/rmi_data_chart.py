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

#SCRAP data
@csrf_exempt
@api_view(['GET'])
def data1_2(request):
    scrap_obj = Scrap_data.objects.all().filter(chart_type = "1week")
    data = []
    # data = [["4/7/2021","551"],["3/11/2021","551.32"],["10/1/2020","301"],["3/15/2021","604"],["4/1/2021","579"],["3/26/2021","580"],["4/8/2021","555"],["4/13/2021","564.98"],["3/31/2021","579"],["3/25/2021","580"],["3/22/2021","597"],["4/14/2021","620"],["3/10/2021","551"],["4/12/2021","565"],["3/30/2021","579"],["3/12/2021","595"],["3/18/2021","590"],["1/10/2020","297"],["1/1/2020","288"],["2/26/2021","580"],["3/19/2021","590"],["12/22/2020","465"]]
    for n in scrap_obj:
        temp= [n.date, n.data]
        data.append(temp)
    # print("data--> ",data)
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        # print(i)
        for j in data:
            # print(j)
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        # i[0] = i[0].replace("/","-")
        date = i[0] #+ " 00:00:00"
        # print(date)
        pattern = '%m-%d-%Y' # %H:%M:%S'
        # print(pattern)
        # os.environ['TZ']='UTC'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        # print(epoch)
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    data = f_data('scrap')
    temp_future_data = data[:6]
    temp = [final_data[-1]]
    future_data = temp + temp_future_data
    
    return Response([final_data,future_data])

@csrf_exempt
@api_view(['GET'])
def data1_3(request):
    scrap_obj = Scrap_data.objects.all().filter(chart_type = "1month")
    data = []
    for n in scrap_obj:
        temp= [n.date, n.data]
        data.append(temp)
    # data = [ [ '5/6/2021', '580' ], [ '5/7/2021', '570' ], [ '5/10/2021', '564' ], [ '5/11/2021', '564.07' ], [ '5/12/2021', '620' ], [ '5/13/2021', '630' ], [ '5/14/2021', '615' ], [ '5/17/2021', '615' ], [ '5/18/2021', '615' ], [ '5/19/2021', '615' ], [ '5/20/2021', '610' ], [ '5/21/2021', '615' ], [ '5/24/2021', '615' ], [ '5/25/2021', '620' ], [ '5/26/2021', '613' ], [ '5/27/2021', '622' ], [ '5/28/2021', '622' ], [ '5/31/2021', None ], [ '6/1/2021', '621' ], [ '6/2/2021', '618' ], [ '6/3/2021', '626' ], [ '6/4/2021', None ] ]
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        # print(i)
        for j in data:
            # print(j)
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        # i[0] = i[0].replace("/","-")
        date = i[0] #+ " 00:00:00"
        # print(date)
        pattern = '%m-%d-%Y' # %H:%M:%S'
        # print(pattern)
        # os.environ['TZ']='UTC'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        # print(epoch)
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    data = f_data('scrap')
    temp_future_data = data[:7]
    temp = [final_data[-1]]
    future_data = temp + temp_future_data
    
    return Response([final_data,future_data])

@csrf_exempt
@api_view(['GET'])
def data1_4(request):
    scrap_obj = Scrap_data.objects.all().filter(chart_type = "3month")
    data = []
    for n in scrap_obj:
        temp= [n.date, n.data]
        data.append(temp)
    # data = [ [ '5/6/2021', '580' ], [ '5/7/2021', '570' ], [ '5/10/2021', '564' ], [ '5/11/2021', '564.07' ], [ '5/12/2021', '620' ], [ '5/13/2021', '630' ], [ '5/14/2021', '615' ], [ '5/17/2021', '615' ], [ '5/18/2021', '615' ], [ '5/19/2021', '615' ], [ '5/20/2021', '610' ], [ '5/21/2021', '615' ], [ '5/24/2021', '615' ], [ '5/25/2021', '620' ], [ '5/26/2021', '613' ], [ '5/27/2021', '622' ], [ '5/28/2021', '622' ], [ '5/31/2021', None ], [ '6/1/2021', '621' ], [ '6/2/2021', '618' ], [ '6/3/2021', '626' ], [ '6/4/2021', None ] ]
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        # print(i)
        for j in data:
            # print(j)
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        # i[0] = i[0].replace("/","-")
        date = i[0] #+ " 00:00:00"
        # print(date)
        pattern = '%m-%d-%Y' # %H:%M:%S'
        # print(pattern)
        # os.environ['TZ']='UTC'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        # print(epoch)
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    data = f_data('scrap')
    temp_future_data = data[:9]
    temp = [final_data[-1]]
    future_data = temp + temp_future_data
    
    return Response([final_data,future_data])

@csrf_exempt
@api_view(['GET'])
def data1_5(request):
    scrap_obj = Scrap_data.objects.all().filter(chart_type = "6month")
    data = []
    for n in scrap_obj:
        temp= [n.date, n.data]
        data.append(temp)
    # data = [ [ '5/6/2021', '580' ], [ '5/7/2021', '570' ], [ '5/10/2021', '564' ], [ '5/11/2021', '564.07' ], [ '5/12/2021', '620' ], [ '5/13/2021', '630' ], [ '5/14/2021', '615' ], [ '5/17/2021', '615' ], [ '5/18/2021', '615' ], [ '5/19/2021', '615' ], [ '5/20/2021', '610' ], [ '5/21/2021', '615' ], [ '5/24/2021', '615' ], [ '5/25/2021', '620' ], [ '5/26/2021', '613' ], [ '5/27/2021', '622' ], [ '5/28/2021', '622' ], [ '5/31/2021', None ], [ '6/1/2021', '621' ], [ '6/2/2021', '618' ], [ '6/3/2021', '626' ], [ '6/4/2021', None ] ]
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        # print(i)
        for j in data:
            # print(j)
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        # i[0] = i[0].replace("/","-")
        date = i[0] #+ " 00:00:00"
        # print(date)
        pattern = '%m-%d-%Y' # %H:%M:%S'
        # print(pattern)
        # os.environ['TZ']='UTC'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        # print(epoch)
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    data = f_data('scrap')
    temp_future_data = data[:12]
    temp = [final_data[-1]]
    future_data = temp + temp_future_data

    return Response([final_data,future_data])

@csrf_exempt
@api_view(['GET'])
def data1_6(request):
    scrap_obj = Scrap_data.objects.all().filter(chart_type = "1year")
    data = []
    for n in scrap_obj:
        temp= [n.date, n.data]
        data.append(temp)
    # data = [ [ '5/6/2021', '580' ], [ '5/7/2021', '570' ], [ '5/10/2021', '564' ], [ '5/11/2021', '564.07' ], [ '5/12/2021', '620' ], [ '5/13/2021', '630' ], [ '5/14/2021', '615' ], [ '5/17/2021', '615' ], [ '5/18/2021', '615' ], [ '5/19/2021', '615' ], [ '5/20/2021', '610' ], [ '5/21/2021', '615' ], [ '5/24/2021', '615' ], [ '5/25/2021', '620' ], [ '5/26/2021', '613' ], [ '5/27/2021', '622' ], [ '5/28/2021', '622' ], [ '5/31/2021', None ], [ '6/1/2021', '621' ], [ '6/2/2021', '618' ], [ '6/3/2021', '626' ], [ '6/4/2021', None ] ]
    # print("data1_6---> ",data)
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])
    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        # print(i)
        for j in data:
            # print(j)
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        # i[0] = i[0].replace("/","-")
        date = i[0] #+ " 00:00:00"
        # print(date)
        pattern = '%m-%d-%Y' # %H:%M:%S'
        # print(pattern)
        # os.environ['TZ']='UTC'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        # print(epoch)
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    data = f_data('scrap')
    temp_future_data = data[:18]
    temp = [final_data[-1]]
    future_data = temp + temp_future_data

    return Response([final_data,future_data])

@csrf_exempt
@api_view(['GET'])
def data1_7(request):
    scrap_obj = Scrap_data.objects.all().filter(chart_type = "2year")
    data = []
    for n in scrap_obj:
        temp= [n.date, n.data]
        data.append(temp)
    # data = [ [ '5/6/2021', '580' ], [ '5/7/2021', '570' ], [ '5/10/2021', '564' ], [ '5/11/2021', '564.07' ], [ '5/12/2021', '620' ], [ '5/13/2021', '630' ], [ '5/14/2021', '615' ], [ '5/17/2021', '615' ], [ '5/18/2021', '615' ], [ '5/19/2021', '615' ], [ '5/20/2021', '610' ], [ '5/21/2021', '615' ], [ '5/24/2021', '615' ], [ '5/25/2021', '620' ], [ '5/26/2021', '613' ], [ '5/27/2021', '622' ], [ '5/28/2021', '622' ], [ '5/31/2021', None ], [ '6/1/2021', '621' ], [ '6/2/2021', '618' ], [ '6/3/2021', '626' ], [ '6/4/2021', None ] ]
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        # print(i)
        for j in data:
            # print(j)
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        # i[0] = i[0].replace("/","-")
        date = i[0] #+ " 00:00:00"
        # print(date)
        pattern = '%m-%d-%Y' # %H:%M:%S'
        # print(pattern)
        # os.environ['TZ']='UTC'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        # print(epoch)
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    data = f_data('scrap')
    temp_future_data = data
    temp = [final_data[-1]]
    future_data = temp + temp_future_data
    
    return Response([final_data,future_data])

#HRC data
@csrf_exempt
@api_view(['GET'])
def data2_2(request):
    hrc_obj = HRC_data.objects.all().filter(chart_type = "1week")
    data = []
    for n in hrc_obj:
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
        # print(i)
        for j in data:
            # print(j)
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        # i[0] = i[0].replace("/","-")
        date = i[0] #+ " 00:00:00"
        # print(date)
        pattern = '%m-%d-%Y' # %H:%M:%S'
        # print(pattern)
        # os.environ['TZ']='UTC'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        # print(epoch)
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    data = f_data('hrc')
    temp_future_data = data[:7]
    temp = [final_data[-1]]
    future_data = temp + temp_future_data
    
    return Response([final_data,future_data])

@csrf_exempt
@api_view(['GET'])
def data2_3(request):
    hrc_obj = HRC_data.objects.all().filter(chart_type = "1month")
    data = []
    for n in hrc_obj:
        temp= [n.date, n.data]
        data.append(temp)
    # data = [ [ '5/6/2021', '1497.2' ], [ '5/7/2021', '1503' ], [ '5/10/2021', '1530.2' ], [ '5/11/2021', '1530.2' ], [ '5/12/2021', '1541.2' ], [ '5/13/2021', '1540.4' ], [ '5/14/2021', '1532.2' ], [ '5/17/2021', '1548.8' ], [ '5/18/2021', '1545.2' ], [ '5/19/2021', '1574.4' ], [ '5/20/2021', '1584.6' ], [ '5/21/2021', '1570.8' ], [ '5/24/2021', '1600.4' ], [ '5/25/2021', '1617.2' ], [ '5/26/2021', '1623' ], [ '5/27/2021', '1632.4' ], [ '5/28/2021', '1609' ], [ '5/31/2021', None ], [ '6/1/2021', '1601.6' ], [ '6/2/2021', '1612.6' ], [ '6/3/2021', '1612.6' ] ]
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        # print(i)
        for j in data:
            # print(j)
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        # i[0] = i[0].replace("/","-")
        date = i[0] #+ " 00:00:00"
        # print(date)
        pattern = '%m-%d-%Y' # %H:%M:%S'
        # print(pattern)
        # os.environ['TZ']='UTC'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        # print(epoch)
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    data = f_data('hrc')
    temp_future_data = data[:8]
    temp = [final_data[-1]]
    future_data = temp + temp_future_data
    
    return Response([final_data,future_data])

@csrf_exempt
@api_view(['GET'])
def data2_4(request):
    hrc_obj = HRC_data.objects.all().filter(chart_type = "3month")
    data = []
    for n in hrc_obj:
        temp= [n.date, n.data]
        data.append(temp)
    # data = [ [ '5/6/2021', '1497.2' ], [ '5/7/2021', '1503' ], [ '5/10/2021', '1530.2' ], [ '5/11/2021', '1530.2' ], [ '5/12/2021', '1541.2' ], [ '5/13/2021', '1540.4' ], [ '5/14/2021', '1532.2' ], [ '5/17/2021', '1548.8' ], [ '5/18/2021', '1545.2' ], [ '5/19/2021', '1574.4' ], [ '5/20/2021', '1584.6' ], [ '5/21/2021', '1570.8' ], [ '5/24/2021', '1600.4' ], [ '5/25/2021', '1617.2' ], [ '5/26/2021', '1623' ], [ '5/27/2021', '1632.4' ], [ '5/28/2021', '1609' ], [ '5/31/2021', None ], [ '6/1/2021', '1601.6' ], [ '6/2/2021', '1612.6' ], [ '6/3/2021', '1612.6' ] ]
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        # print(i)
        for j in data:
            # print(j)
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        # i[0] = i[0].replace("/","-")
        date = i[0] #+ " 00:00:00"
        # print(date)
        pattern = '%m-%d-%Y' # %H:%M:%S'
        # print(pattern)
        # os.environ['TZ']='UTC'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        # print(epoch)
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    data = f_data('hrc')
    temp_future_data = data[:9]
    temp = [final_data[-1]]
    future_data = temp + temp_future_data
    
    return Response([final_data,future_data])

@csrf_exempt
@api_view(['GET'])
def data2_5(request):
    hrc_obj = HRC_data.objects.all().filter(chart_type = "6month")
    data = []
    for n in hrc_obj:
        temp= [n.date, n.data]
        data.append(temp)
    # data = [ [ '5/6/2021', '1497.2' ], [ '5/7/2021', '1503' ], [ '5/10/2021', '1530.2' ], [ '5/11/2021', '1530.2' ], [ '5/12/2021', '1541.2' ], [ '5/13/2021', '1540.4' ], [ '5/14/2021', '1532.2' ], [ '5/17/2021', '1548.8' ], [ '5/18/2021', '1545.2' ], [ '5/19/2021', '1574.4' ], [ '5/20/2021', '1584.6' ], [ '5/21/2021', '1570.8' ], [ '5/24/2021', '1600.4' ], [ '5/25/2021', '1617.2' ], [ '5/26/2021', '1623' ], [ '5/27/2021', '1632.4' ], [ '5/28/2021', '1609' ], [ '5/31/2021', None ], [ '6/1/2021', '1601.6' ], [ '6/2/2021', '1612.6' ], [ '6/3/2021', '1612.6' ] ]
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        # print(i)
        for j in data:
            # print(j)
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        # i[0] = i[0].replace("/","-")
        date = i[0] #+ " 00:00:00"
        # print(date)
        pattern = '%m-%d-%Y' # %H:%M:%S'
        # print(pattern)
        # os.environ['TZ']='UTC'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        # print(epoch)
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    data = f_data('hrc')
    temp_future_data = data[:13]
    temp = [final_data[-1]]
    future_data = temp + temp_future_data
    
    return Response([final_data,future_data])

@csrf_exempt
@api_view(['GET'])
def data2_6(request):
    hrc_obj = HRC_data.objects.all().filter(chart_type = "1year")
    data = []
    for n in hrc_obj:
        temp= [n.date, n.data]
        data.append(temp)
    # data = [ [ '5/6/2021', '1497.2' ], [ '5/7/2021', '1503' ], [ '5/10/2021', '1530.2' ], [ '5/11/2021', '1530.2' ], [ '5/12/2021', '1541.2' ], [ '5/13/2021', '1540.4' ], [ '5/14/2021', '1532.2' ], [ '5/17/2021', '1548.8' ], [ '5/18/2021', '1545.2' ], [ '5/19/2021', '1574.4' ], [ '5/20/2021', '1584.6' ], [ '5/21/2021', '1570.8' ], [ '5/24/2021', '1600.4' ], [ '5/25/2021', '1617.2' ], [ '5/26/2021', '1623' ], [ '5/27/2021', '1632.4' ], [ '5/28/2021', '1609' ], [ '5/31/2021', None ], [ '6/1/2021', '1601.6' ], [ '6/2/2021', '1612.6' ], [ '6/3/2021', '1612.6' ] ]
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        # print(i)
        for j in data:
            # print(j)
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        # i[0] = i[0].replace("/","-")
        date = i[0] #+ " 00:00:00"
        # print(date)
        pattern = '%m-%d-%Y' # %H:%M:%S'
        # print(pattern)
        # os.environ['TZ']='UTC'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        # print(epoch)
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    data = f_data('hrc')
    temp_future_data = data[:19]
    temp = [final_data[-1]]
    future_data = temp + temp_future_data
    
    return Response([final_data,future_data])

@csrf_exempt
@api_view(['GET'])
def data2_7(request):
    hrc_obj = HRC_data.objects.all().filter(chart_type = "2year")
    data = []
    for n in hrc_obj:
        temp= [n.date, n.data]
        data.append(temp)
    # data = [ [ '5/6/2021', '1497.2' ], [ '5/7/2021', '1503' ], [ '5/10/2021', '1530.2' ], [ '5/11/2021', '1530.2' ], [ '5/12/2021', '1541.2' ], [ '5/13/2021', '1540.4' ], [ '5/14/2021', '1532.2' ], [ '5/17/2021', '1548.8' ], [ '5/18/2021', '1545.2' ], [ '5/19/2021', '1574.4' ], [ '5/20/2021', '1584.6' ], [ '5/21/2021', '1570.8' ], [ '5/24/2021', '1600.4' ], [ '5/25/2021', '1617.2' ], [ '5/26/2021', '1623' ], [ '5/27/2021', '1632.4' ], [ '5/28/2021', '1609' ], [ '5/31/2021', None ], [ '6/1/2021', '1601.6' ], [ '6/2/2021', '1612.6' ], [ '6/3/2021', '1612.6' ] ]
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        # print(i)
        for j in data:
            # print(j)
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        # i[0] = i[0].replace("/","-")
        date = i[0] #+ " 00:00:00"
        # print(date)
        pattern = '%m-%d-%Y' # %H:%M:%S'
        # print(pattern)
        # os.environ['TZ']='UTC'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        # print(epoch)
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    data = f_data('hrc')
    temp_future_data = data
    temp = [final_data[-1]]
    future_data = temp + temp_future_data
    
    return Response([final_data,future_data])

#IRON ORE data
@csrf_exempt
@api_view(['GET'])
def data3_2(request):
    hrc_obj = iron_data.objects.all().filter(chart_type = "1week")
    data = []
    for n in hrc_obj:
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
        # print(i)
        for j in data:
            # print(j)
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        # i[0] = i[0].replace("/","-")
        date = i[0] #+ " 00:00:00"
        # print(date)
        pattern = '%m-%d-%Y' # %H:%M:%S'
        # print(pattern)
        # os.environ['TZ']='UTC'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        # print(epoch)
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    data = f_data('iron')
    temp_future_data = data[:7]
    temp = [final_data[-1]]
    future_data = temp + temp_future_data
    
    return Response([final_data,future_data])

@csrf_exempt
@api_view(['GET'])
def data3_3(request):
    hrc_obj = iron_data.objects.all().filter(chart_type = "1month")
    data = []
    for n in hrc_obj:
        temp= [n.date, n.data]
        data.append(temp)
    # data = [ [ '5/6/2021', '1497.2' ], [ '5/7/2021', '1503' ], [ '5/10/2021', '1530.2' ], [ '5/11/2021', '1530.2' ], [ '5/12/2021', '1541.2' ], [ '5/13/2021', '1540.4' ], [ '5/14/2021', '1532.2' ], [ '5/17/2021', '1548.8' ], [ '5/18/2021', '1545.2' ], [ '5/19/2021', '1574.4' ], [ '5/20/2021', '1584.6' ], [ '5/21/2021', '1570.8' ], [ '5/24/2021', '1600.4' ], [ '5/25/2021', '1617.2' ], [ '5/26/2021', '1623' ], [ '5/27/2021', '1632.4' ], [ '5/28/2021', '1609' ], [ '5/31/2021', None ], [ '6/1/2021', '1601.6' ], [ '6/2/2021', '1612.6' ], [ '6/3/2021', '1612.6' ] ]
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        # print(i)
        for j in data:
            # print(j)
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        # i[0] = i[0].replace("/","-")
        date = i[0] #+ " 00:00:00"
        # print(date)
        pattern = '%m-%d-%Y' # %H:%M:%S'
        # print(pattern)
        # os.environ['TZ']='UTC'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        # print(epoch)
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    data = f_data('iron')
    temp_future_data = data[:8]
    temp = [final_data[-1]]
    future_data = temp + temp_future_data
    
    return Response([final_data,future_data])

@csrf_exempt
@api_view(['GET'])
def data3_4(request):
    hrc_obj = iron_data.objects.all().filter(chart_type = "3month")
    data = []
    for n in hrc_obj:
        temp= [n.date, n.data]
        data.append(temp)
    # data = [ [ '5/6/2021', '1497.2' ], [ '5/7/2021', '1503' ], [ '5/10/2021', '1530.2' ], [ '5/11/2021', '1530.2' ], [ '5/12/2021', '1541.2' ], [ '5/13/2021', '1540.4' ], [ '5/14/2021', '1532.2' ], [ '5/17/2021', '1548.8' ], [ '5/18/2021', '1545.2' ], [ '5/19/2021', '1574.4' ], [ '5/20/2021', '1584.6' ], [ '5/21/2021', '1570.8' ], [ '5/24/2021', '1600.4' ], [ '5/25/2021', '1617.2' ], [ '5/26/2021', '1623' ], [ '5/27/2021', '1632.4' ], [ '5/28/2021', '1609' ], [ '5/31/2021', None ], [ '6/1/2021', '1601.6' ], [ '6/2/2021', '1612.6' ], [ '6/3/2021', '1612.6' ] ]
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        # print(i)
        for j in data:
            # print(j)
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        # i[0] = i[0].replace("/","-")
        date = i[0] #+ " 00:00:00"
        # print(date)
        pattern = '%m-%d-%Y' # %H:%M:%S'
        # print(pattern)
        # os.environ['TZ']='UTC'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        # print(epoch)
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    data = f_data('iron')
    temp_future_data = data[:9]
    temp = [final_data[-1]]
    future_data = temp + temp_future_data
    
    return Response([final_data,future_data])

@csrf_exempt
@api_view(['GET'])
def data3_5(request):
    hrc_obj = iron_data.objects.all().filter(chart_type = "6month")
    data = []
    for n in hrc_obj:
        temp= [n.date, n.data]
        data.append(temp)
    # data = [ [ '5/6/2021', '1497.2' ], [ '5/7/2021', '1503' ], [ '5/10/2021', '1530.2' ], [ '5/11/2021', '1530.2' ], [ '5/12/2021', '1541.2' ], [ '5/13/2021', '1540.4' ], [ '5/14/2021', '1532.2' ], [ '5/17/2021', '1548.8' ], [ '5/18/2021', '1545.2' ], [ '5/19/2021', '1574.4' ], [ '5/20/2021', '1584.6' ], [ '5/21/2021', '1570.8' ], [ '5/24/2021', '1600.4' ], [ '5/25/2021', '1617.2' ], [ '5/26/2021', '1623' ], [ '5/27/2021', '1632.4' ], [ '5/28/2021', '1609' ], [ '5/31/2021', None ], [ '6/1/2021', '1601.6' ], [ '6/2/2021', '1612.6' ], [ '6/3/2021', '1612.6' ] ]
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        # print(i)
        for j in data:
            # print(j)
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        # i[0] = i[0].replace("/","-")
        date = i[0] #+ " 00:00:00"
        # print(date)
        pattern = '%m-%d-%Y' # %H:%M:%S'
        # print(pattern)
        # os.environ['TZ']='UTC'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        # print(epoch)
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    data = f_data('iron')
    temp_future_data = data[:13]
    temp = [final_data[-1]]
    future_data = temp + temp_future_data
    
    return Response([final_data,future_data])

@csrf_exempt
@api_view(['GET'])
def data3_6(request):
    hrc_obj = iron_data.objects.all().filter(chart_type = "1year")
    data = []
    for n in hrc_obj:
        temp= [n.date, n.data]
        data.append(temp)
    # data = [ [ '5/6/2021', '1497.2' ], [ '5/7/2021', '1503' ], [ '5/10/2021', '1530.2' ], [ '5/11/2021', '1530.2' ], [ '5/12/2021', '1541.2' ], [ '5/13/2021', '1540.4' ], [ '5/14/2021', '1532.2' ], [ '5/17/2021', '1548.8' ], [ '5/18/2021', '1545.2' ], [ '5/19/2021', '1574.4' ], [ '5/20/2021', '1584.6' ], [ '5/21/2021', '1570.8' ], [ '5/24/2021', '1600.4' ], [ '5/25/2021', '1617.2' ], [ '5/26/2021', '1623' ], [ '5/27/2021', '1632.4' ], [ '5/28/2021', '1609' ], [ '5/31/2021', None ], [ '6/1/2021', '1601.6' ], [ '6/2/2021', '1612.6' ], [ '6/3/2021', '1612.6' ] ]
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        # print(i)
        for j in data:
            # print(j)
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        # i[0] = i[0].replace("/","-")
        date = i[0] #+ " 00:00:00"
        # print(date)
        pattern = '%m-%d-%Y' # %H:%M:%S'
        # print(pattern)
        # os.environ['TZ']='UTC'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        # print(epoch)
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    data = f_data('iron')
    temp_future_data = data[:19]
    temp = [final_data[-1]]
    future_data = temp + temp_future_data
    
    return Response([final_data,future_data])

@csrf_exempt
@api_view(['GET'])
def data3_7(request):
    hrc_obj = iron_data.objects.all().filter(chart_type = "2year")
    data = []
    for n in hrc_obj:
        temp= [n.date, n.data]
        data.append(temp)
    # data = [ [ '5/6/2021', '1497.2' ], [ '5/7/2021', '1503' ], [ '5/10/2021', '1530.2' ], [ '5/11/2021', '1530.2' ], [ '5/12/2021', '1541.2' ], [ '5/13/2021', '1540.4' ], [ '5/14/2021', '1532.2' ], [ '5/17/2021', '1548.8' ], [ '5/18/2021', '1545.2' ], [ '5/19/2021', '1574.4' ], [ '5/20/2021', '1584.6' ], [ '5/21/2021', '1570.8' ], [ '5/24/2021', '1600.4' ], [ '5/25/2021', '1617.2' ], [ '5/26/2021', '1623' ], [ '5/27/2021', '1632.4' ], [ '5/28/2021', '1609' ], [ '5/31/2021', None ], [ '6/1/2021', '1601.6' ], [ '6/2/2021', '1612.6' ], [ '6/3/2021', '1612.6' ] ]
    date = []
    final_data = []
    for i in data:
        i[0] = i[0].replace("/","-")
        date.append(i[0])

    date.sort(key = lambda date: datetime.strptime(date, '%m-%d-%Y'))
    # print(date)
    final_data = []
    for i in date:
        # print(i)
        for j in data:
            # print(j)
            if j[0] == i:
                tmp = []
                tmp.append(i)
                tmp.append(j[1])
                final_data.append(tmp)
                break

    for i in final_data:
        # i[0] = i[0].replace("/","-")
        date = i[0] #+ " 00:00:00"
        # print(date)
        pattern = '%m-%d-%Y' # %H:%M:%S'
        # print(pattern)
        # os.environ['TZ']='UTC'
        epoch = int(time.mktime(time.strptime(date, pattern)))
        # print(epoch)
        i[0] = epoch*1000
        if i[1]!=None:
            i[1] = float(i[1])
    
    data = f_data('iron')
    temp_future_data = data
    temp = [final_data[-1]]
    future_data = temp + temp_future_data
    
    return Response([final_data,future_data])


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

