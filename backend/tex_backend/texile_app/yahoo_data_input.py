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
import yfinance as yf
# from currency_converter import CurrencyConverter
# c = CurrencyConverter()
# from forex_python.converter import CurrencyRates
# c = CurrencyRates()
from py_currency_converter import convert

#all data pull
@csrf_exempt
@api_view(['GET'])
def y_data_pull(request):
    chart_list = ["RS","RIO","VALE","MT","PKX","NUE","TS","STLD","CLF","TX","GGB","X","CMC","SXC","TMST","BHP","NWPX","HO=F","RB=F"]
    chart_list_EUR = ["VK.PA","TKA.DE","SZG.DE"]
    chart_list_JPY = ["5411.T","5401.T"]

    for each in chart_list:
        y_finance(each)
        y_stock_data(each)
    for each in chart_list_EUR:
        y_finance_EUR(each)
        y_stock_data_EUR(each)
    for each in chart_list_JPY:
        y_finance_JPY(each)
        y_stock_data_JPY(each)
    return Response({"status":200})

#function for pulling data from the yahoo finance website
def y_finance(comp):
    yahoo_data.objects.filter(chart = comp).delete()
    print("start pulling data for", comp)
    #1 week
    co_obj = yf.Ticker(comp)
    list_date = []
    list_data = []
    final_data = []
    hist = co_obj.history(period="1wk")
    data = hist["Close"]
    hist.reset_index(inplace = True)
    for each in hist["Date"]:
        date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
        list_date.append(date)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    l = len(list_data)
    for i in range(0,l):
        temp_list = [list_date[i],list_data[i]]
        final_data.append(temp_list)
    # print(final_data)
    for n in final_data:
        # print(n[1])
        yahoo_obj = yahoo_data(chart = comp ,chart_type = '1week' , data = n[1], date = n[0])
        yahoo_obj.save()
    print("1 week done")

    # yahoo_data.objects.filter(chart = comp).delete()
    # print("start pulling data for", comp)
    # #1 week
    # y_data_hourly.objects.filter(chart = comp).delete()
    # co_obj = yf.Ticker('TS')
    # list_date = []
    # list_data = []
    # list_time=[]
    # final_data = []
    # hist = co_obj.history(interval="1h")
    # # print(hist.index.array)
    # date=hist.index.array
    # # print(date)
    # data = hist["Close"]
    # for i in range(len(date)):
    #     # print(data[i],date[i])
    #     date_final = datetime.strptime(str(date[i]), "%Y-%m-%d %H:%M:%S-%V:%W").strftime("%Y-%m-%d")
        
    #     time_final = datetime.strptime(str(date[i]), "%Y-%m-%d %H:%M:%S-%V:%W").strftime("%Y-%m-%d %H:%M:%S")
    #     # print(time_final)
    #     list_date.append(date_final)
    #     # print(list_date)
    #     list_time.append(time_final)
    #     list_data.append(round(data[i],2))
    # # print(date,final_data)
    # l = len(list_data)
    # for i in range(0,l):
    #   temp_list = [list_date[i],list_data[i],list_time[i]]
    #   final_data.append(temp_list)
    # # print("final data",final_data)
    # for n in final_data:
    #     # print(n[1])
    #    y_data = y_data_hourly(chart = comp ,chart_type = '1week' , data = n[1], date = n[0],time=n[2])
    #    y_data.save()
    # print("1 week done")

    # hist.reset_index(inplace = True)
    # for each in hist["Date"]:
    #     date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
    #     list_date.append(date)
    # for each in data:
    #     data = round(each,2)
    #     list_data.append(data)
    # l = len(list_data)
    # for i in range(0,l):
    #     temp_list = [list_date[i],list_data[i]]
    #     final_data.append(temp_list)
    # # print(final_data)
    # for n in final_data:
    #     # print(n[1])
    #     yahoo_obj = yahoo_data(chart = comp ,chart_type = '1week' , data = n[1], date = n[0])
    #     yahoo_obj.save()
    # print("1 week done")

    #1 month
    co_obj = yf.Ticker(comp)
    list_date = []
    list_data = []
    final_data = []
    hist = co_obj.history(period="1mo")
    data = hist["Close"]
    hist.reset_index(inplace = True)
    for each in hist["Date"]:
        date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
        list_date.append(date)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    l = len(list_data)
    for i in range(0,l):
        temp_list = [list_date[i],list_data[i]]
        final_data.append(temp_list)
    # print(final_data)
    for n in final_data:
        # print(n[1])
        yahoo_obj = yahoo_data(chart = comp ,chart_type = '1month' , data = n[1], date = n[0])
        yahoo_obj.save()
    print("1 month done")
    
    #3months
    co_obj = yf.Ticker(comp)
    list_date = []
    list_data = []
    final_data = []
    hist = co_obj.history(period="3mo")
    data = hist["Close"]
    hist.reset_index(inplace = True)
    for each in hist["Date"]:
        date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
        list_date.append(date)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    l = len(list_data)
    for i in range(0,l):
        temp_list = [list_date[i],list_data[i]]
        final_data.append(temp_list)
    # print(final_data)
    for n in final_data:
        # print(n[1])
        yahoo_obj = yahoo_data(chart = comp ,chart_type = '3month' , data = n[1], date = n[0])
        yahoo_obj.save()
    print("3 month done")

    #6months
    co_obj = yf.Ticker(comp)
    list_date = []
    list_data = []
    final_data = []
    hist = co_obj.history(period="6mo")
    data = hist["Close"]
    hist.reset_index(inplace = True)
    for each in hist["Date"]:
        date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
        list_date.append(date)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    l = len(list_data)
    for i in range(0,l):
        temp_list = [list_date[i],list_data[i]]
        final_data.append(temp_list)
    # print(final_data)
    for n in final_data:
        # print(n[1])
        yahoo_obj = yahoo_data(chart = comp ,chart_type = '6month' , data = n[1], date = n[0])
        yahoo_obj.save()
    print("6 month done")

    #1 year
    co_obj = yf.Ticker(comp)
    list_date = []
    list_data = []
    final_data = []
    hist = co_obj.history(period="1y")
    data = hist["Close"]
    hist.reset_index(inplace = True)
    for each in hist["Date"]:
        date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
        list_date.append(date)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    l = len(list_data)
    for i in range(0,l):
        temp_list = [list_date[i],list_data[i]]
        final_data.append(temp_list)
    # print(final_data)
    for n in final_data:
        # print(n[1])
        yahoo_obj = yahoo_data(chart = comp ,chart_type = '1year' , data = n[1], date = n[0])
        yahoo_obj.save()
    print("1 year done")

    #2 year
    co_obj = yf.Ticker(comp)
    list_date = []
    list_data = []
    final_data = []
    hist = co_obj.history(period="2y")
    data = hist["Close"]
    hist.reset_index(inplace = True)
    for each in hist["Date"]:
        date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
        list_date.append(date)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    l = len(list_data)
    for i in range(0,l):
        temp_list = [list_date[i],list_data[i]]
        final_data.append(temp_list)
    # print(final_data)
    for n in final_data:
        # print(n[1])
        yahoo_obj = yahoo_data(chart = comp ,chart_type = '2year' , data = n[1], date = n[0])
        yahoo_obj.save()    
    print("2 year done")

    print(comp," done")

def y_stock_data(comp):
    stock_data.objects.filter(chart_type = comp).delete()
    co_obj = yf.Ticker(comp)
    list_data = []
    hist = co_obj.history(period="1mo")
    data = hist["Close"]
    # print(data)
    # hist.reset_index(inplace = True)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    # print(list_data)
    diff = (list_data[-1] - list_data[-2])
    # print(diff)
    diff_per = round(((diff/list_data[-2])*100), 2)
    # print(diff_per)
    data_obj = stock_data(chart_type = comp , data = diff_per, current = round(list_data[-1],2))
    data_obj.save()
    print(comp, "stock data done")
    insert_updated_time(comp)

# EUR to USD
def y_finance_EUR(comp):
    yahoo_data.objects.filter(chart = comp).delete()
    print("start pulling data for", comp)
    #1 week
    co_obj = yf.Ticker(comp)
    list_date = []
    list_data = []
    final_data = []
    hist = co_obj.history(period="1wk")
    data = hist["Close"]
    hist.reset_index(inplace = True)
    for each in hist["Date"]:
        date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
        list_date.append(date)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    l = len(list_data)
    for i in range(0,l):
        temp_list = [list_date[i],list_data[i]]
        final_data.append(temp_list)
    # print(final_data)
    for n in final_data:
        # print(n[1])
        val = n[1]
        val = convert(base='EUR', amount=val, to=['USD'])['USD']
        #val = temp['USD']
        val = round(val,2)
        # print(val)
        yahoo_obj = yahoo_data(chart = comp ,chart_type = '1week' , data = val, date = n[0])
        yahoo_obj.save()
    print("1 week done")

    #1 month
    co_obj = yf.Ticker(comp)
    list_date = []
    list_data = []
    final_data = []
    hist = co_obj.history(period="1mo")
    data = hist["Close"]
    hist.reset_index(inplace = True)
    for each in hist["Date"]:
        date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
        list_date.append(date)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    l = len(list_data)
    for i in range(0,l):
        temp_list = [list_date[i],list_data[i]]
        final_data.append(temp_list)
    # print(final_data)
    for n in final_data:
        # print(n[1])
        val = n[1]
        val = convert(base='EUR', amount=val, to=['USD'])['USD']
        #val = temp['USD']
        val = round(val,2)
        yahoo_obj = yahoo_data(chart = comp ,chart_type = '1month' , data = val, date = n[0])
        yahoo_obj.save()
    print("1 month done")
    
    #3months
    co_obj = yf.Ticker(comp)
    list_date = []
    list_data = []
    final_data = []
    hist = co_obj.history(period="3mo")
    data = hist["Close"]
    hist.reset_index(inplace = True)
    for each in hist["Date"]:
        date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
        list_date.append(date)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    l = len(list_data)
    for i in range(0,l):
        temp_list = [list_date[i],list_data[i]]
        final_data.append(temp_list)
    # print(final_data)
    for n in final_data:
        # print(n[1])
        val = n[1]
        val = convert(base='EUR', amount=val, to=['USD'])['USD']
        #val = temp['USD']
        val = round(val,2)
        yahoo_obj = yahoo_data(chart = comp ,chart_type = '3month' , data = val, date = n[0])
        yahoo_obj.save()
    print("3 month done")

    #6months
    co_obj = yf.Ticker(comp)
    list_date = []
    list_data = []
    final_data = []
    hist = co_obj.history(period="6mo")
    data = hist["Close"]
    hist.reset_index(inplace = True)
    for each in hist["Date"]:
        date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
        list_date.append(date)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    l = len(list_data)
    for i in range(0,l):
        temp_list = [list_date[i],list_data[i]]
        final_data.append(temp_list)
    # print(final_data)
    for n in final_data:
        # print(n[1])
        val = n[1]
        val = convert(base='EUR', amount=val, to=['USD'])['USD']
        #val = temp['USD']
        val = round(val,2)
        yahoo_obj = yahoo_data(chart = comp ,chart_type = '6month' , data = val, date = n[0])
        yahoo_obj.save()
    print("6 month done")

    #1 year
    co_obj = yf.Ticker(comp)
    list_date = []
    list_data = []
    final_data = []
    hist = co_obj.history(period="1y")
    data = hist["Close"]
    hist.reset_index(inplace = True)
    for each in hist["Date"]:
        date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
        list_date.append(date)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    l = len(list_data)
    for i in range(0,l):
        temp_list = [list_date[i],list_data[i]]
        final_data.append(temp_list)
    # print(final_data)
    for n in final_data:
        # print(n[1])
        val = n[1]
        val = convert(base='EUR', amount=val, to=['USD'])['USD']
        #val = temp['USD']
        val = round(val,2)
        yahoo_obj = yahoo_data(chart = comp ,chart_type = '1year' , data = val, date = n[0])
        yahoo_obj.save()
    print("1 year done")

    #2 year
    co_obj = yf.Ticker(comp)
    list_date = []
    list_data = []
    final_data = []
    hist = co_obj.history(period="2y")
    data = hist["Close"]
    hist.reset_index(inplace = True)
    for each in hist["Date"]:
        date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
        list_date.append(date)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    l = len(list_data)
    for i in range(0,l):
        temp_list = [list_date[i],list_data[i]]
        final_data.append(temp_list)
    # print(final_data)
    for n in final_data:
        # print(n[1])
        val = n[1]
        val = convert(base='EUR', amount=val, to=['USD'])['USD']
        #val = temp['USD']
        val = round(val,2)
        yahoo_obj = yahoo_data(chart = comp ,chart_type = '2year' , data = val, date = n[0])
        yahoo_obj.save()    
    print("2 year done")

    print(comp," done")

def y_stock_data_EUR(comp):
    stock_data.objects.filter(chart_type = comp).delete()
    co_obj = yf.Ticker(comp)
    list_data = []
    hist = co_obj.history(period="1mo")
    data = hist["Close"]
    # print(data)
    # hist.reset_index(inplace = True)
    for each in data:
        val = round(each,2)
        val = convert(base='EUR', amount=val, to=['USD'])['USD']
        #val = temp['USD']
        list_data.append(val)
    # print(list_data)
    diff = (list_data[-1] - list_data[-2])
    # print(diff)
    diff_per = round(((diff/list_data[-2])*100), 2)
    # print(diff_per)
    data_obj = stock_data(chart_type = comp , data = diff_per, current = round(list_data[-1],2))
    data_obj.save()
    print(comp, "stock data done")
    insert_updated_time(comp)

# JPY to USD
def y_finance_JPY(comp):
    yahoo_data.objects.filter(chart = comp).delete()
    print("start pulling data for", comp)
    #1 week
    co_obj = yf.Ticker(comp)
    list_date = []
    list_data = []
    final_data = []
    hist = co_obj.history(period="1wk")
    data = hist["Close"]
    hist.reset_index(inplace = True)
    for each in hist["Date"]:
        date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
        list_date.append(date)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    l = len(list_data)
    for i in range(0,l):
        temp_list = [list_date[i],list_data[i]]
        final_data.append(temp_list)
    # print(final_data)
    for n in final_data:
        # print(n[1])
        val = n[1]
        val = convert(base='JPY', amount=val, to=['USD'])['USD']
        #val = temp['USD']
        val = round(val,2)
        yahoo_obj = yahoo_data(chart = comp ,chart_type = '1week' , data = val, date = n[0])
        yahoo_obj.save()
    print("1 week done")

    #1 month
    co_obj = yf.Ticker(comp)
    list_date = []
    list_data = []
    final_data = []
    hist = co_obj.history(period="1mo")
    data = hist["Close"]
    hist.reset_index(inplace = True)
    for each in hist["Date"]:
        date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
        list_date.append(date)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    l = len(list_data)
    for i in range(0,l):
        temp_list = [list_date[i],list_data[i]]
        final_data.append(temp_list)
    # print(final_data)
    for n in final_data:
        # print(n[1])
        val = n[1]
        val = convert(base='JPY', amount=val, to=['USD'])['USD']
        #val = temp['USD']
        val = round(val,2)
        yahoo_obj = yahoo_data(chart = comp ,chart_type = '1month' , data = val, date = n[0])
        yahoo_obj.save()
    print("1 month done")
    
    #3months
    co_obj = yf.Ticker(comp)
    list_date = []
    list_data = []
    final_data = []
    hist = co_obj.history(period="3mo")
    data = hist["Close"]
    hist.reset_index(inplace = True)
    for each in hist["Date"]:
        date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
        list_date.append(date)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    l = len(list_data)
    for i in range(0,l):
        temp_list = [list_date[i],list_data[i]]
        final_data.append(temp_list)
    # print(final_data)
    for n in final_data:
        # print(n[1])
        val = n[1]
        val = convert(base='JPY', amount=val, to=['USD'])['USD']
        #val = temp['USD']
        val = round(val,2)
        yahoo_obj = yahoo_data(chart = comp ,chart_type = '3month' , data = val, date = n[0])
        yahoo_obj.save()
    print("3 month done")

    #6months
    co_obj = yf.Ticker(comp)
    list_date = []
    list_data = []
    final_data = []
    hist = co_obj.history(period="6mo")
    data = hist["Close"]
    hist.reset_index(inplace = True)
    for each in hist["Date"]:
        date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
        list_date.append(date)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    l = len(list_data)
    for i in range(0,l):
        temp_list = [list_date[i],list_data[i]]
        final_data.append(temp_list)
    # print(final_data)
    for n in final_data:
        # print(n[1])
        val = n[1]
        val = convert(base='JPY', amount=val, to=['USD'])['USD']
        #val = temp['USD']
        val = round(val,2)
        yahoo_obj = yahoo_data(chart = comp ,chart_type = '6month' , data = val, date = n[0])
        yahoo_obj.save()
    print("6 month done")

    #1 year
    co_obj = yf.Ticker(comp)
    list_date = []
    list_data = []
    final_data = []
    hist = co_obj.history(period="1y")
    data = hist["Close"]
    hist.reset_index(inplace = True)
    for each in hist["Date"]:
        date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
        list_date.append(date)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    l = len(list_data)
    for i in range(0,l):
        temp_list = [list_date[i],list_data[i]]
        final_data.append(temp_list)
    # print(final_data)
    for n in final_data:
        # print(n[1])
        val = n[1]
        val = convert(base='JPY', amount=val, to=['USD'])['USD']
        #val = temp['USD']
        val = round(val,2)
        yahoo_obj = yahoo_data(chart = comp ,chart_type = '1year' , data = val, date = n[0])
        yahoo_obj.save()
    print("1 year done")

    #2 year
    co_obj = yf.Ticker(comp)
    list_date = []
    list_data = []
    final_data = []
    hist = co_obj.history(period="2y")
    data = hist["Close"]
    hist.reset_index(inplace = True)
    for each in hist["Date"]:
        date = datetime.strptime(str(each), "%Y-%m-%d %H:%M:%S").strftime('%m-%d-%Y')
        list_date.append(date)
    for each in data:
        data = round(each,2)
        list_data.append(data)
    l = len(list_data)
    for i in range(0,l):
        temp_list = [list_date[i],list_data[i]]
        final_data.append(temp_list)
    # print(final_data)
    for n in final_data:
        # print(n[1])
        val = n[1]
        val = convert(base='JPY', amount=val, to=['USD'])['USD']
        #val = temp['USD']
        val = round(val,2)
        yahoo_obj = yahoo_data(chart = comp ,chart_type = '2year' , data = val, date = n[0])
        yahoo_obj.save()    
    print("2 year done")

    print(comp," done")

def y_stock_data_JPY(comp):
    stock_data.objects.filter(chart_type = comp).delete()
    co_obj = yf.Ticker(comp)
    list_data = []
    hist = co_obj.history(period="1mo")
    data = hist["Close"]
    # print(data)
    # hist.reset_index(inplace = True)
    for each in data:
        val = round(each,2)
        val = convert(base='JPY', amount=val, to=['USD'])['USD']
        #val = temp['USD']
        list_data.append(val)
    # print(list_data)
    diff = (list_data[-1] - list_data[-2])
    # print(diff)
    diff_per = round(((diff/list_data[-2])*100), 2)
    # print(diff_per)
    data_obj = stock_data(chart_type = comp , data = diff_per, current = round(list_data[-1],2))
    data_obj.save()
    print(comp, "stock data done")
    insert_updated_time(comp)


def insert_updated_time(comp):
    dt = datetime.now(tz=timezone.utc)
    try:
        a = updated_time.objects.get(chart = comp)
        a.update_time = dt
        a.save()
    except:
        data_obj = updated_time(chart = comp, update_time = dt)
        data_obj.save()

##########################Depricated#################################

    # y_finance("RIO")
    # y_stock_data("RIO")
    # y_finance("VALE")
    # y_stock_data("VALE")
    # y_finance("MT")
    # y_stock_data("MT")
    # y_finance("PKX")
    # y_stock_data("PKX")
    # y_finance("NUE")
    # y_stock_data("NUE")
    # y_finance("TS")
    # y_stock_data("TS")
    # y_finance("STLD")
    # y_stock_data("STLD")
    # y_finance("RS")
    # y_stock_data("RS")
    # y_finance("CLF")
    # y_stock_data("CLF")
    # y_finance("TX")
    # y_stock_data("TX")
    # y_finance("GGB")
    # y_stock_data("GGB")
    # y_finance("X")
    # y_stock_data("X")
    # y_finance("CMC")
    # y_stock_data("CMC")
    # y_finance("SXC")
    # y_stock_data("SXC")
    # y_finance("TMST")
    # y_stock_data("TMST")
    # y_finance("BHP")
    # y_stock_data("BHP")
    # y_finance("HO=F")
    # y_stock_data("HO=F")
    # y_finance("RB=F")
    # y_stock_data("RB=F")
    # # y_finance("MFF=F") #coal
    # # y_stock_data("MFF=F")
    # # y_finance("MFFH22.NYM") #coal
    # # y_stock_data("MFFH22.NYM")
    # y_finance("NWPX")
    # y_stock_data("NWPX")
    # y_finance_EUR("VK.PA")
    # y_stock_data_EUR("VK.PA")
    # y_finance_EUR("TKA.DE")
    # y_stock_data_EUR("TKA.DE")
    # y_finance_EUR("SZG.DE")
    # y_stock_data_EUR("SZG.DE")
    # y_finance_JPY("5401.T") #nippon
    # y_stock_data_JPY("5401.T")
    # y_finance_JPY("5411.T")
    # y_stock_data_JPY("5411.T")
