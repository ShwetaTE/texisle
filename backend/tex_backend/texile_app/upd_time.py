from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
import json
from django.core import serializers
import time as tm
import os
from datetime import datetime
import datetime

# last updated timestamp
@api_view(['POST'])
def up_time(request):
    chart= request.data["chart"]
    updated_time_obj = updated_time.objects.filter(chart = chart)
    up_time = updated_time_obj[0].update_time
    # print(time)
    time = date_format(up_time)
    # print(time)
    return Response({"time":time})

def date_format(date):
    b = date.replace(tzinfo=None)
    # print("b--> ",b)
    a = datetime.datetime.now().replace(microsecond=0)
    # print("a--> ",a)
    date = a-b
    converted_date=str(date).split(',')
    # print(converted_date)
    if len(converted_date)>1:
        if int(converted_date[0].split(' ')[0])<1:
            time=converted_date[1].split(':')[0]+" Hr"
        else:
            time=converted_date[0]
    else:
        if int(converted_date[0].split(':')[0])==0:
            if converted_date[0].split(':')[1]=='00':
                temp=int(converted_date[0].split(':')[2])
                time=str(temp) +" sec"
            else:
                temp=int(converted_date[0].split(':')[1])
                time=str(temp) + " min"
        else:
            temp=int(converted_date[0].split(':')[0])
            time=str(temp)+" Hr"
    # print(time)
    time = time + " ago"
    return(time)