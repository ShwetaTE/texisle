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
# from models import customMessage
@api_view(['POST'])
def message(request):
    title= request.data["title"]
    app= request.data["app"]
    message_obj = customMessage.objects.filter(app = app, title = title)
    for each in message_obj:
        msg = each.message
    print(msg)
    return Response({'message': msg})
@api_view(['POST'])
def createMessage(request):
    title=request.data["title"]
    app=request.data["app"]
    message=request.data["message"]
    custommessage =customMessage(app=app ,title=title ,message=message)
    custommessage.save()
    # print(title,app,message)
    return Response({message})
@api_view(['GET'])
def getMessage(request):
    custommessage=customMessage.objects.all()
    list=[]
    for i in range (0,len(custommessage)):
        list.append([custommessage[i].title,custommessage[i].message])
    # print(list)
    return Response(list)


