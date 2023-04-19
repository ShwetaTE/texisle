from tabnanny import check
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from newspaper.extractors import RE_LANG
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
from django_pandas.io import read_frame
from numpy import ERR_CALL
import pandas as pd
import pandas_market_calendars as mcal
import numpy as np
import time, os
from datetime import datetime
from datetime import datetime, timedelta, date
from django.utils import timezone
from .smtp_server import feedback_mail
import after_response

# api to store the feedback submitted on the app. 
# Also sends the feedback as email to the email id's present on the texile_app.email table
@api_view(['POST'])
def feedback_data(request):
    name = request.data["name"]
    phone = request.data["phone"]
    comment = request.data["comment"]
    email = request.data['email']
    rating = request.data["rating"]
    deviceID = request.data['deviceID']
    app = request.data["app_type"]

    data_obj = feedback(deviceID = deviceID, Name = name, email = email, PhoneNo = phone, Comment = comment, Rating = rating, app = app)
    data_obj.save()
    feedback_mail.after_response(request)
    return Response({"status":200})

@api_view(['POST'])
def check_feedback(request):
    deviceID = request.data['deviceID']
    app = request.data['app']
    data_obj = feedback.objects.filter(deviceID = deviceID, app = app)
    len = data_obj.count()
    if len!=0:
        return Response({'status':200})
    else:
        customer_obj = customer_table.objects.get(deviceID = deviceID, app = app)
        created_time = customer_obj.created_time
        # print(created_time)
        b = created_time.replace(tzinfo=None)
        a = datetime.now().replace(microsecond=0)
        date = a-b
        print(date)
        converted_date=str(date).split(',')
        # print(findLen(converted_date))
        diff_len = findLen(converted_date)
        if diff_len > 1:
            # print(converted_date[0].split(' '))
            day_diff = converted_date[0].split(' ')[0]
        if diff_len == 1:
            # print(converted_date[0].split(' '))
            day_diff = 0
        print(day_diff)
        # print(converted_date[0].split(' '))
        # if converted_date[0][-1] == 's':
        #     print(converted_date[0].split(' '))
        return Response({'status':300, 'Diff': day_diff})

def findLen(string):
    return sum( 1 for i in string);