from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from newspaper.extractors import RE_LANG
from pymysql import NULL
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
from django_pandas.io import read_frame
from django.utils import timezone
import requests
import time, os
from datetime import datetime
import after_response

# api to record session usage data
@api_view(['PUT'])
def app_ended(request):
    session_id = request.data['session_id']
    app = request.data['app_type']
    timer = request.data['timer']
    page = request.data['page']
    deviceID = request.data['deviceID']
    try:
        timer = int(timer)
    except:
        timer = 0
    # print(page)
    data_insert.after_response(session_id, app, timer, page, deviceID);
    # click_data.after_response(session_id, app, page, deviceID);

    return Response({"status":200})

@api_view(['PUT'])
def page_count(request):
    session_id = request.data['session_id']
    app = request.data['app_type']
    page = request.data['page']
    deviceID = request.data['deviceID']
    click_data.after_response(session_id, app, page, deviceID);

    return Response({"status":200})


@after_response.enable
def data_insert(session_id, app, timer, page, deviceID):
    dt = datetime.now(tz=timezone.utc)
    try:
        a = session_usage.objects.get(session_id = session_id, deviceID = deviceID)
        a.app = app
        temp_time = a.time
        upd_time = int(temp_time) + int(timer)
        a.time = upd_time
        a.save()
    except:
        data_obj = session_usage(deviceID = deviceID, session_id = session_id, app = app, time = timer, created_time = dt)
        data_obj.save()

    try:
        b = session_page_usage_new.objects.get(session_id = session_id, deviceID = deviceID)
        b.app = app
        if page == 'lp':
            temp_time = b.landing_page
            upd_time = int(temp_time) + int(timer)
            b.landing_page = upd_time
            b.save()
        elif page == 'iom':
            temp_time = b.iom_page
            upd_time = int(temp_time) + int(timer)
            b.iom_page = upd_time
            b.save()
        elif page == 't':
            temp_time = b.t_page
            upd_time = int(temp_time) + int(timer)
            b.t_page = upd_time
            b.save()
        elif page == 'smf':
            temp_time = b.smf_page
            upd_time = int(temp_time) + int(timer)
            b.smf_page = upd_time
            b.save()
        elif page == 'pmf':
            temp_time = b.pmf_page
            upd_time = int(temp_time) + int(timer)
            b.pmf_page = upd_time
            b.save()
        elif page == 'rmi':
            temp_time = b.rmi_page
            upd_time = int(temp_time) + int(timer)
            b.rmi_page = upd_time
            b.save()
        elif page == 'carbon_offset':
            temp_time = b.carbon_offset
            upd_time = int(temp_time) + int(timer)
            b.carbon_offset = upd_time
            b.save()
        elif page == 'watchlist' or page == 'watchlist_setting':
            temp_time = b.watchlist
            upd_time = int(temp_time) + int(timer)
            b.watchlist = upd_time
            b.save()
        elif page == 'feedback':
            temp_time = b.feedback
            upd_time = int(temp_time) + int(timer)
            b.feedback = upd_time
            b.save()
        elif page == 'about_v2' or page == 'about':
            temp_time = b.about
            upd_time = int(temp_time) + int(timer)
            b.about = upd_time
            b.save()
        elif page == 'tutorial':
            temp_time = b.tutorial
            upd_time = int(temp_time) + int(timer)
            b.tutorial = upd_time
            b.save()
        elif page == 'rc':
            temp_time = b.rc_page
            upd_time = int(temp_time) + int(timer)
            b.rc_page = upd_time
            b.save()
        elif page == 'wc':
            temp_time = b.wc_page
            upd_time = int(temp_time) + int(timer)
            b.wc_page = upd_time
            b.save()
    except:
        if page == 'lp':
            data_obj = session_page_usage_new(deviceID = deviceID, session_id = session_id, app = app, landing_page = timer)
            data_obj.save()
        elif page == 'iom':
            data_obj = session_page_usage_new(deviceID = deviceID, session_id = session_id, app = app, iom_page = timer)
            data_obj.save()
        elif page == 't':
            data_obj = session_page_usage_new(deviceID = deviceID, session_id = session_id, app = app, t_page = timer)
            data_obj.save()
        elif page == 'smf':
            data_obj = session_page_usage_new(deviceID = deviceID, session_id = session_id, app = app, smf_page = timer)
            data_obj.save()
        elif page == 'pmf':
            data_obj = session_page_usage_new(deviceID = deviceID, session_id = session_id, app = app, pmf_page = timer)
            data_obj.save()
        elif page == 'rmi':
            data_obj = session_page_usage_new(deviceID = deviceID, session_id = session_id, app = app, rmi_page = timer)
            data_obj.save()
        elif page == 'carbon_offset':
            data_obj = session_page_usage_new(deviceID = deviceID, session_id = session_id, app = app, carbon_offset = timer)
            data_obj.save()
        elif page == 'watchlist' or page == 'watchlist_setting':
            data_obj = session_page_usage_new(deviceID = deviceID, session_id = session_id, app = app, watchlist = timer)
            data_obj.save()
        elif page == 'feedback':
            data_obj = session_page_usage_new(deviceID = deviceID, session_id = session_id, app = app, feedback = timer)
            data_obj.save()
        elif page == 'about' or page == 'about_v2':
            data_obj = session_page_usage_new(deviceID = deviceID, session_id = session_id, app = app, about = timer)
            data_obj.save()
        elif page == 'tutorial':
            data_obj = session_page_usage_new(deviceID = deviceID, session_id = session_id, app = app, tutorial = timer)
            data_obj.save()
        elif page == 'rc':
            data_obj = session_page_usage_new(deviceID = deviceID, session_id = session_id, app = app, rc_page = timer)
            data_obj.save()
        elif page == 'wc':
            data_obj = session_page_usage_new(deviceID = deviceID, session_id = session_id, app = app, wc_page = timer)
            data_obj.save()

#number of clicks
@after_response.enable
def click_data(session_id, app, page, deviceID):
    try:
        b = device_page_clicks.objects.get(session_id = session_id, deviceID = deviceID)
        b.app = app
        if page == 'lp':
            temp_time = b.landing_page
            upd_time = int(temp_time) + 1
            b.landing_page = upd_time
            b.save()
        elif page == 'iom':
            temp_time = b.iom_page
            upd_time = int(temp_time) + 1
            b.iom_page = upd_time
            b.save()
        elif page == 't':
            temp_time = b.t_page
            upd_time = int(temp_time) + 1
            b.t_page = upd_time
            b.save()
        elif page == 'smf':
            temp_time = b.smf_page
            upd_time = int(temp_time) + 1
            b.smf_page = upd_time
            b.save()
        elif page == 'pmf':
            temp_time = b.pmf_page
            upd_time = int(temp_time) + 1
            b.pmf_page = upd_time
            b.save()
        elif page == 'rmi':
            temp_time = b.rmi_page
            upd_time = int(temp_time) + 1
            b.rmi_page = upd_time
            b.save()
        elif page == 'carbon_offset':
            temp_time = b.carbon_offset
            upd_time = int(temp_time) + 1
            b.carbon_offset = upd_time
            b.save()
        elif page == 'watchlist' or page == 'watchlist_setting':
            temp_time = b.watchlist
            upd_time = int(temp_time) + 1
            b.watchlist = upd_time
            b.save()
        elif page == 'feedback':
            temp_time = b.feedback
            upd_time = int(temp_time) + 1
            b.feedback = upd_time
            b.save()
        elif page == 'about_v2' or page == 'about':
            temp_time = b.about
            upd_time = int(temp_time) + 1
            b.about = upd_time
            b.save()
        elif page == 'tutorial':
            temp_time = b.tutorial
            upd_time = int(temp_time) + 1
            b.tutorial = upd_time
            b.save()
        elif page == 'rc':
            temp_time = b.rc_page
            upd_time = int(temp_time) + 1
            b.rc_page = upd_time
            b.save()
        elif page == 'wc':
            temp_time = b.wc_page
            upd_time = int(temp_time) + 1
            b.wc_page = upd_time
            b.save()
    except:
        if page == 'lp':
            data_obj = device_page_clicks(deviceID = deviceID, session_id = session_id, app = app, landing_page = 1)
            data_obj.save()
        elif page == 'iom':
            data_obj = device_page_clicks(deviceID = deviceID, session_id = session_id, app = app, iom_page = 1)
            data_obj.save()
        elif page == 't':
            data_obj = device_page_clicks(deviceID = deviceID, session_id = session_id, app = app, t_page = 1)
            data_obj.save()
        elif page == 'smf':
            data_obj = device_page_clicks(deviceID = deviceID, session_id = session_id, app = app, smf_page = 1)
            data_obj.save()
        elif page == 'pmf':
            data_obj = device_page_clicks(deviceID = deviceID, session_id = session_id, app = app, pmf_page = 1)
            data_obj.save()
        elif page == 'rmi':
            data_obj = device_page_clicks(deviceID = deviceID, session_id = session_id, app = app, rmi_page = 1)
            data_obj.save()
        elif page == 'carbon_offset':
            data_obj = device_page_clicks(deviceID = deviceID, session_id = session_id, app = app, carbon_offset = 1)
            data_obj.save()
        elif page == 'watchlist' or page == 'watchlist_setting':
            data_obj = device_page_clicks(deviceID = deviceID, session_id = session_id, app = app, watchlist = 1)
            data_obj.save()
        elif page == 'feedback':
            data_obj = device_page_clicks(deviceID = deviceID, session_id = session_id, app = app, feedback = 1)
            data_obj.save()
        elif page == 'about' or page == 'about_v2':
            data_obj = device_page_clicks(deviceID = deviceID, session_id = session_id, app = app, about = 1)
            data_obj.save()
        elif page == 'tutorial':
            data_obj = device_page_clicks(deviceID = deviceID, session_id = session_id, app = app, tutorial = 1)
            data_obj.save()
        elif page == 'rc':
            data_obj = device_page_clicks(deviceID = deviceID, session_id = session_id, app = app, rc_page = 1)
            data_obj.save()
        elif page == 'wc':
            data_obj = device_page_clicks(deviceID = deviceID, session_id = session_id, app = app, wc_page = 1)
            data_obj.save()