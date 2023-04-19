from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
from django.utils import timezone
import time, os
from datetime import datetime,timedelta
import pandas_market_calendars as mcal
# import datetime
import requests
import json
import pandas as pd
from full_fred.fred import Fred
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

#data pull for transport tickers
@api_view(['GET'])
def transport_data_pull(request):
    baltic_data_daily()
    truckT_data()
    CassFreight_data()
    # usld_data()
    all_grade_data()
    return Response({"status":200})

@api_view(['GET'])
def baltic_data_pull(request):
    baltic_data_daily()
    return Response({"status":200})

# data for ulsd, mainly comes through azure function
@api_view(['POST'])
def usld_data(request):
    data = request.data["data"]
    print(data)
    date_list = fetch_date()
    print(date_list)
    date_len = len(date_list)
    if date_len!=0:
        date = date_list[0][0]
        data_obj = transportation_data(date = date, data = data, chart = "ULSD")
        data_obj.save()
        stock_diff("ULSD")
        insert_updated_time("ULSD")
        return Response({"status":200})
    else:
        return Response({"status":500})

def baltic_data_daily():
    try:
        url = "https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols=.BADI&requestMethod=itv&noform=1&partnerId=2&fund=1&exthrs=1&output=json&events=1"
        response = requests.request("GET", url, headers={}, data={})

        res = json.loads(response.text)
        data = res["FormattedQuoteResult"]["FormattedQuote"][0]["last"]
        data = float(data.replace(',', ''))
        print(data)
        date = fetch_date()[0][0]
        print(date)

        baltic_data =  transportation_data.objects.filter(chart = "Baltic").last()
        temp_date = baltic_data.date
        print(temp_date)
        if temp_date == date:        
            print("no new data")
        else:
            print("new data")
            data_obj = transportation_data(date = date, data = data, chart = "Baltic")
            data_obj.save()    
            stock_diff("Baltic")
            insert_updated_time("Baltic")
    except Exception as e:
        err = "Error: " + str(e)
        # print("oops")
        url = "http://localhost:8000/texisle-app/send_mail/"
        payload={'content': 'Issue with daily Baltic data pull\n'+ err}
        response = requests.request("POST", url, headers={}, data=payload, files={})

def truckT_data():
    # print(file_dir)
    fred = Fred(file_dir +'/fred_api_key.txt')
    fred.set_api_key_file(file_dir + '/fred_api_key.txt')
    df = fred.get_series_df('CEU4348400001')
    df = df.sort_index(ascending=False)
    df_f = df.iloc[:1]
    final = df_f[['date', 'value']]
    f_df = final.iloc[::-1]
    f_list = f_df.values.tolist()
    for each in f_list:
        dt = each[0] 
        date_time = datetime.strptime(dt, "%Y-%m-%d")
        if date_time.weekday() == 5:
            date_time = date_time + timedelta(days=2)
        if date_time.weekday() == 6:
            date_time = date_time + timedelta(days=1)
        dt = date_time.strftime('%m-%d-%Y') 
        each[0] = dt
    truckT_list = f_list
    truck_data =  transportation_data.objects.filter(chart = "Truck").last()
    temp_date = truck_data.date
    if each[0] == temp_date:
        print("no new data")
    else:
        for each in truckT_list:
            data_obj = transportation_data(date = each[0], data = each[1], chart = "Truck")
            data_obj.save()         
        # stock_diff("Truck")        
        stock_val("Truck")
        insert_updated_time("Truck")

def CassFreight_data():
    # print(file_dir)
    fred = Fred(file_dir +'/fred_api_key.txt')
    fred.set_api_key_file(file_dir + '/fred_api_key.txt')
    df = fred.get_series_df('FRGSHPUSM649NCIS')
    df = df.sort_index(ascending=False)
    df_f = df.iloc[:1]
    final = df_f[['date', 'value']]
    f_df = final.iloc[::-1]
    f_list = f_df.values.tolist()
    # print(f_list)
    for each in f_list:
        dt = each[0] 
        date_time = datetime.strptime(dt, "%Y-%m-%d")
        if date_time.weekday() == 5:
            date_time = date_time + timedelta(days=2)
        if date_time.weekday() == 6:
            date_time = date_time + timedelta(days=1)
        dt = date_time.strftime('%m-%d-%Y') 
        each[0] = dt
    CF_list = f_list
    # print(CF_list)
    CF_data =  transportation_data.objects.filter(chart = "CassFreight").last()
    temp_date = CF_data.date
    # print(temp_date)
    if each[0] == temp_date:
        print("no new data")
    else:
        print("new data")
        for each in CF_list:
            data_obj = transportation_data(date = each[0], data = each[1], chart = "CassFreight")
            data_obj.save()         
        # stock_diff("CassFreight")   
        stock_val("CassFreight")
        insert_updated_time("CassFreight")

def all_grade_data():
    url = "https://api.eia.gov/series/?api_key=YLHXnjHw9q4O41DGwQikaMKIWVyLDczPgFzijclZ&series_id=PET.EMM_EPM0_PTE_NUS_DPG.W"
    response = requests.request("GET", url, headers={}, data={})

    res = json.loads(response.text)
    data = res["series"]
    f_data = data[0]["data"]
    for each in f_data:
        dt = each[0]
        date_time = datetime.strptime(dt, "%Y%m%d")
        dt = date_time.strftime('%m-%d-%Y') 
        each[0] = dt
    all_grade_data = f_data[:1]
    AG_df = pd.DataFrame(all_grade_data)
    # AG_df = AG_df.iloc[::-1]
    upd_list = AG_df.values.tolist()
    print(upd_list)
    ag_data =  transportation_data.objects.filter(chart = "All-Grade").last()
    temp_date = ag_data.date
    if temp_date == upd_list[0][0]:        
        print("no new data")
    else:
        print("new data")
        for each in upd_list:
            data_obj = transportation_data(date = each[0], data = round(each[1],2), chart = "All-Grade")
            data_obj.save()
        stock_diff("All-Grade")
        insert_updated_time("All-Grade")

def stock_diff(ticker):
    data_obj = transportation_data.objects.filter(chart = ticker)
    list_data = []
    for each in data_obj:
        data = each.data
        date = each.date
        temp = [date, data]
        list_data.append(temp)
    val1 = float(list_data[-1][1])
    val2 = float(list_data[-2][1])
    diff = (val1 - val2)
    # print(diff)
    diff_per = round((diff/val2*100), 2)
    # print(diff_per)
    stock_data.objects.filter(chart_type = ticker).delete()
    data_obj = stock_data(chart_type = ticker , data = diff_per, current = round(val1,2))
    data_obj.save()
    return()

def stock_val(ticker):
    data_obj = transportation_data.objects.filter(chart = ticker)
    list_data = []
    for each in data_obj:
        data = each.data
        date = each.date
        temp = [date, data]
        list_data.append(temp)
    val1 = float(list_data[-1][1])
    val2 = float(list_data[-2][1])
    diff = (val1 - val2)
    # print(diff)
    diff_per = round((diff/val2*100), 2)
    # print(diff_per)
    stock_data.objects.filter(chart_type = ticker).delete()
    data_obj = stock_data(chart_type = ticker , data = diff, current = round(val1,2))
    data_obj.save()
    return()

def insert_updated_time(comp):
    dt = datetime.now(tz=timezone.utc)
    try:
        a = updated_time.objects.get(chart = comp)
        a.update_time = dt
        a.save()
    except:
        data_obj = updated_time(chart = comp, update_time = dt)
        data_obj.save()


def fetch_date():
    presentday = datetime.now()
    d = datetime.today().weekday()
    if d == 0:
        date = presentday - timedelta(days = 3)
    else:
        date = presentday - timedelta(days = 1)
    dt = date.strftime('%Y-%m-%d')
    # print(dt)
    # Create a calendar
    nyse = mcal.get_calendar('NYSE')
    early = nyse.schedule(start_date=dt, end_date=dt)
    print(early)
    date_list = []
    list = mcal.date_range(early, frequency='1D')
    # print(list)
    for each in list:
        dt = each.strftime('%m-%d-%Y')
        date_list.append(dt)
    date_df = pd.DataFrame(date_list, columns =['date'])
    date_df.rename(columns = {'date':'Date'}, inplace = True)
    date_list = date_df.values.tolist()
    print(date_list)
    return(date_list)
    