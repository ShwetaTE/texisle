from cmath import exp
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
import json
from django.core import serializers
from django.utils import timezone
import time, os
from datetime import datetime
import requests
import yfinance as yf
# from currency_converter import CurrencyConverter
# c = CurrencyConverter()
# from forex_python.converter import CurrencyRates
# c = CurrencyRates()
from py_currency_converter import convert

#hourly data pull yahoo
@api_view(['GET'])
def pull_latest_data(request):
    eur = convert(base='EUR', amount=1, to=['USD'])['USD'] 
    jpy = convert(base='JPY', amount=1, to=['USD'])['USD']

    chart_list = ["RIO","VALE","MT","PKX","NUE","TS","STLD","RS","CLF","TX","GGB","X","CMC","SXC","TMST","BHP","NWPX"]
    chart_list_EUR = ["VK.PA","TKA.DE","SZG.DE"]
    chart_list_JPY = ["5411.T","5401.T"]

    for each in chart_list:
        y_finance_input(each)
    for each in chart_list_EUR:
        y_finance_input_EUR(each, eur)
    for each in chart_list_JPY:
        y_finance_input_JPY(each, jpy)

    return Response({"status":200})

@api_view(['GET'])
def pull_data_us(request):
    chart_list = ["RIO","VALE","MT","PKX","NUE","TS","STLD","RS","CLF","TX","GGB","X","CMC","SXC","TMST","BHP","NWPX"]
    for each in chart_list:
        y_finance_input(each)

    return Response({"status":200})

@api_view(['GET'])
def pull_data_eur(response):
    eur = convert(base='EUR', amount=1, to=['USD'])['USD'] 
    chart_list_EUR = ["VK.PA","TKA.DE","SZG.DE"]
    for each in chart_list_EUR:
        y_finance_input_EUR(each, eur)
    return Response({"status":200})

@api_view(['GET'])
def pull_data_jpy(response):
    jpy = convert(base='JPY', amount=1, to=['USD'])['USD'] 
    chart_list_JPY = ["5411.T","5401.T"]
    for each in chart_list_JPY:
        y_finance_input_JPY(each, jpy)
    return Response({"status":200})


#function for pulling data from the yahoo finance website
def y_finance_input(comp):
    try:
        # print("start pulling data for", comp)

        co_obj = yf.Ticker(comp)
        list_date = []
        list_data = []
        final_data = []
        hist = co_obj.history(period="1d")
        data = hist["Close"]
        hist.reset_index(inplace = True)
        # print(data)
        for each in hist["Date"]:
            date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
            list_date.append(date)
        for each in data:
            data = round(each,2)
            list_data.append(data)
        l = len(list_data)
        for i in range(0,l):
            temp_list = [list_date[i],list_data[i]]
            final_data=temp_list
        # print(final_data)
        # print(n[1])

        insert_data("1week",comp, final_data[0], final_data[1])
        # print("1 week done")

        insert_data("1month",comp, final_data[0], final_data[1])
        # print("1 month done")

        insert_data("3month",comp, final_data[0], final_data[1])
        # print("3 month done")

        insert_data("6month",comp, final_data[0], final_data[1])
        # print("6 month done")

        insert_data("1year",comp, final_data[0], final_data[1])
        # print("1 year done")

        insert_data("2year",comp, final_data[0], final_data[1])
        # print("2 year done")

        y_stock_data_input(comp)
        insert_updated_time(comp)
        hourly_data_save(final_data[1], final_data[0], comp)
        print(comp," done")
    except Exception as e:
        err = "Error: " + str(e)
        print(err)
        print("No data for ", comp)
        url = "http://localhost:8000/texisle-app/send_mail/"
        payload={'content': 'Issue with hourly'+ comp +'data pull\n'+ err}
        response = requests.request("POST", url, headers={}, data=payload, files={})

def y_stock_data_input(comp):
    # stock_data.objects.filter(chart_type = comp).delete()
    co_obj = yf.Ticker(comp)
    list_data = []
    hist = co_obj.history(period="1mo")
    data = hist["Close"]
    for each in data:
        data = round(each,2)
        list_data.append(data)
    diff = (list_data[-1] - list_data[-2])
    diff_per = round(((diff/list_data[-2])*100), 2)
    # print(diff_per)
    # data_obj = stock_data(chart_type = comp , data = diff_per, current = round(list_data[-1],2))
    data_obj = stock_data.objects.get(chart_type = comp)
    data_obj.data = diff_per
    data_obj.current = round(list_data[-1],2)
    data_obj.save()
    # print(comp, "stock data done")

# EUR to USD
def y_finance_input_EUR(comp, eur):
    try:
        # print("start pulling data for", comp)

        co_obj = yf.Ticker(comp)
        list_date = []
        list_data = []
        final_data = []
        hist = co_obj.history(period="1d")
        data = hist["Close"]
        hist.reset_index(inplace = True)
        # print(data)
        for each in hist["Date"]:
            date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
            list_date.append(date)
        for each in data:
            data = round(each,2)
            list_data.append(data)
        l = len(list_data)
        for i in range(0,l):
            temp_list = [list_date[i],list_data[i]]
            final_data=temp_list
        val = final_data[1]
        # print(val)
        # val = convert(base='EUR', amount=val, to=['USD'])['USD']
        val = val*eur
        val = round(val,2)
        # print(final_data)
        # print(n[1])

        insert_data("1week",comp, final_data[0], val)
        # print("1 week done")

        insert_data("1month",comp, final_data[0], val)
        # print("1 month done")

        insert_data("3month",comp, final_data[0], val)
        # print("3 month done")

        insert_data("6month",comp, final_data[0], val)
        # print("6 month done")

        insert_data("1year",comp, final_data[0], val)
        # print("1 year done")

        insert_data("2year",comp, final_data[0], val)
        # print("2 year done")

        y_stock_data_input_EUR(comp, eur)
        insert_updated_time(comp)
        hourly_data_save(val, final_data[0], comp)
        print(comp," done")
    except Exception as e:
        err = "Error: " + str(e)
        print(err)
        print("No data for ",comp)
        url = "http://localhost:8000/texisle-app/send_mail/"
        payload={'content': 'Issue with hourly '+ comp +' data pull\n'+ err}
        response = requests.request("POST", url, headers={}, data=payload, files={})

def y_stock_data_input_EUR(comp, eur):
    # stock_data.objects.filter(chart_type = comp).delete()
    co_obj = yf.Ticker(comp)
    list_data = []
    hist = co_obj.history(period="1mo")
    data = hist["Close"]
    for each in data:
        val = round(each,2)
        # val = convert(base='EUR', amount=val, to=['USD'])['USD']
        val = val*eur
        list_data.append(val)
    diff = (list_data[-1] - list_data[-2])
    diff_per = round(((diff/list_data[-2])*100), 2)
    # print(diff_per)
    # data_obj = stock_data(chart_type = comp , data = diff_per, current = round(list_data[-1],2))
    data_obj = stock_data.objects.get(chart_type = comp)
    data_obj.data = diff_per
    data_obj.current = round(list_data[-1],2)
    data_obj.save()
    # print(comp, "stock data done")

# JPY to USD
def y_finance_input_JPY(comp, jpy):
    try:
        # print("start pulling data for", comp)

        co_obj = yf.Ticker(comp)
        list_date = []
        list_data = []
        final_data = []
        hist = co_obj.history(period="1d")
        data = hist["Close"]
        hist.reset_index(inplace = True)
        # print(data)
        for each in hist["Date"]:
            date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
            list_date.append(date)
        for each in data:
            data = round(each,2)
            list_data.append(data)
        l = len(list_data)
        for i in range(0,l):
            temp_list = [list_date[i],list_data[i]]
            final_data=temp_list
        val = final_data[1]
        # val = convert(base='JPY', amount=val, to=['USD'])['USD']
        val = val*jpy
        val = round(val,2)
        # print(final_data)
        # print(n[1])

        insert_data("1week",comp, final_data[0], val)
        # print("1 week done")

        insert_data("1month",comp, final_data[0], val)
        # print("1 month done")

        insert_data("3month",comp, final_data[0], val)
        # print("3 month done")

        insert_data("6month",comp, final_data[0], val)
        # print("6 month done")

        insert_data("1year",comp, final_data[0], val)
        # print("1 year done")

        insert_data("2year",comp, final_data[0], val)
        # print("2 year done")

        y_stock_data_input_JPY(comp, jpy)
        insert_updated_time(comp)
        hourly_data_save(val, final_data[0], comp)
        print(comp," done")
    except Exception as e:
        err = "Error: " + str(e)
        print("No data for ",comp)
        url = "http://localhost:8000/texisle-app/send_mail/"
        payload={'content': 'Issue with hourly'+ comp +'data pull\n'+ err}
        response = requests.request("POST", url, headers={}, data=payload, files={})

def y_stock_data_input_JPY(comp, jpy):
    # stock_data.objects.filter(chart_type = comp).delete()
    co_obj = yf.Ticker(comp)
    list_data = []
    hist = co_obj.history(period="1mo")
    data = hist["Close"]
    for each in data:
        val = round(each,2)
        # val = convert(base='JPY', amount=val, to=['USD'])['USD']
        val = val*jpy
        list_data.append(val)
    diff = (list_data[-1] - list_data[-2])
    diff_per = round(((diff/list_data[-2])*100), 2)
    # print(diff_per)
    # data_obj = stock_data(chart_type = comp , data = diff_per, current = round(list_data[-1],2))
    data_obj = stock_data.objects.get(chart_type = comp)
    data_obj.data = diff_per
    data_obj.current = round(list_data[-1],2)
    data_obj.save()
    # print(comp, "stock data done")


def insert_data(span, comp, date, data):
    try:
        # print("try block")
        yahoo_obj = yahoo_data.objects.get(chart = comp ,chart_type = span, date = date)    #date already exists
        # article = yahoo_data.objects.filter(chart = comp ,chart_type = span).first()
        # print("data ",article.data)
        yahoo_obj.data = data
        yahoo_obj.save()
    except:
        # print("except block")
        yahoo_obj = yahoo_data(chart = comp ,chart_type = span, data = data, date = date)   #date doesn't exist
        yahoo_obj.save()
        article = yahoo_data.objects.filter(chart = comp ,chart_type = span).first()
        if article:
            article.delete()
        
def insert_updated_time(comp):
    dt = datetime.now(tz=timezone.utc)
    try:
        a = updated_time.objects.get(chart = comp)
        a.update_time = dt
        a.save()
    except:
        data_obj = updated_time(chart = comp, update_time = dt)
        data_obj.save()

def hourly_data_save(val, date,chart_type):
    dt = datetime.now()
    if val>0:
        data_obj = hourly_yahoo_data(date = date, val = round(val,2), chart = chart_type, update_time = dt)
        data_obj.save()

############Depricated##############

    # y_finance_input("RIO")
    # y_finance_input("VALE")
    # y_finance_input("MT")
    # y_finance_input("PKX")
    # y_finance_input("NUE")
    # y_finance_input("TS")
    # y_finance_input("STLD")
    # y_finance_input("RS")
    # y_finance_input("CLF")
    # y_finance_input("TX")
    # y_finance_input("GGB")
    # y_finance_input("X")
    # y_finance_input("CMC")
    # y_finance_input("SXC")
    # y_finance_input("TMST")
    # y_finance_input("BHP")
    # # y_finance_input("HO=F")
    # # y_finance_input("RB=F")
    # # y_finance_input("MFF=F") #coal
    # # y_finance_input("MFFH22.NYM") #coal
    # y_finance_input("NWPX")
    # y_finance_input_EUR("VK.PA")
    # y_finance_input_EUR("TKA.DE")
    # y_finance_input_EUR("SZG.DE")
    # y_finance_input_JPY("5401.T") #nippon
    # y_finance_input_JPY("5411.T") #JFE