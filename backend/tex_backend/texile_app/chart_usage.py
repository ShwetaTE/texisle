from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
from django.utils import timezone
import time, os
from datetime import datetime,timedelta
# import datetime
import requests
import json
import pandas as pd
import os
import sys

# stores the numbeer of visits per chart
@api_view(['POST'])
def update_chart_count(request):
    try:
        chart = request.data["chart"]
        deviceID = request.data["deviceID"]
        app = request.data['app']
        insert_chart_data(chart, deviceID, app)
        try:
            session_id = request.data['session_id']
            insert_session_chart_data(chart, deviceID, app, session_id)
        except:
            print("no session id")

    except:
        chart = request.data["chart"]
        insert_data(chart)
    return Response({'status': 200})

def insert_chart_data(chart, deviceID, app):
    try:
        chart_obj = device_chart_usage.objects.get(chart = chart, deviceID = deviceID, app = app)    #deviceID and chart already exists
        visits = chart_obj.visits
        visits = visits + 1
        chart_obj.visits = visits
        chart_obj.save()
    except:
        # print("except block")
        chart_obj = device_chart_usage(app = app, deviceID = deviceID, chart = chart , visits = 1)   #deviceID doesn't exist
        chart_obj.save()

def insert_session_chart_data(chart, deviceID, app, session_id):
    try:
        chart_obj = device_session_chart_usage.objects.get(chart = chart, deviceID = deviceID, app = app, session_id = session_id)    #deviceID, session_id and chart already exists
        visits = chart_obj.visits
        visits = visits + 1
        chart_obj.visits = visits
        chart_obj.save()
    except:
        # print("except block")
        chart_obj = device_session_chart_usage(app = app, deviceID = deviceID, session_id = session_id, chart = chart , visits = 1)   #deviceID and session_id doesn't exist
        chart_obj.save()

def insert_data(chart):
    try:
        # print("try block")
        yahoo_obj = chart_usage.objects.get(chart = chart)    #chart already exists
        visits = yahoo_obj.visits
        visits = visits + 1
        yahoo_obj.visits = visits
        yahoo_obj.save()
    except:
        # print("except block")
        yahoo_obj = chart_usage(chart = chart , visits = 1)   #chart doesn't exist
        yahoo_obj.save()