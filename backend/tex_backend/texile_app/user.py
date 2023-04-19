from ensurepip import version
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

# update the customer table
@api_view(['POST'])
def customer(request):
    app = request.data['app_type']
    deviceID = request.data['deviceID']
    app_vr = request.data['app_vr']
    os = request.data['os']
    try:
        terms_vr = request.data['terms_vr']
        first_installed_vr = request.data['app_vr']
    except:
        terms_vr = 1
        first_installed_vr = "1.3.15"
    dt = datetime.now(tz=timezone.utc)

    try:
        a = customer_table.objects.get(deviceID = deviceID, app = app)
        a.Terms = "Y"
        a.vr = app_vr
        a.terms_vr = terms_vr
        a.save()
        print("customer present")
    except:
        data_obj = customer_table(deviceID = deviceID, app = app, created_time = dt, Terms = "Y", vr = app_vr, os =os, terms_vr = terms_vr, first_installed_vr = first_installed_vr )
        data_obj.save()

    return Response({"status":200})

# update the terms column in the customer table
@api_view(['POST'])
def remove_terms(request):
    app = request.data['app_type']
    deviceID = request.data['deviceID']
    dt = datetime.now(tz=timezone.utc)
    try:
        a = customer_table.objects.get(deviceID = deviceID, app = app)
        a.Terms = "N"
        a.save()
        print("customer present")
    except:
        data_obj = customer_table(deviceID = deviceID, app = app, created_time = dt, Terms = "N")
        data_obj.save()
    return Response({"status":200})

# check if the terms is accepted
@api_view(['POST'])
def check_terms(request):
    app = request.data['app_type']
    deviceID = request.data['deviceID']
    app_vr = request.data['app_vr']
    try:
        terms_vr = request.data['terms_vr']
    except:
        terms_vr = 1

    try:
        data_obj = customer_table.objects.get(deviceID = deviceID, app = app)
        db_terms_vr = data_obj.terms_vr
        vr = data_obj.vr
        if app_vr == vr:
            terms = "Y"
        else:
            if int(db_terms_vr) == int(terms_vr):
                terms = "Y"
                data_obj.Terms = "Y"
                data_obj.vr = app_vr
                data_obj.terms_vr = terms_vr
                data_obj.save()
            else:
                terms = "N"
    except:
        terms = "N"
    return Response({"terms":terms})
