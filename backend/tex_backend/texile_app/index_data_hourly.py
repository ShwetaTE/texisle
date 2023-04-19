from ast import expr_context
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from newspaper.extractors import RE_LANG
from django.utils import timezone
from texile_app.index_data import iom_data
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
from django_pandas.io import read_frame
import requests
from numpy import ERR_CALL
import pandas_market_calendars as mcal
import yfinance as yf
import pandas as pd
import numpy as np
import time, os
from datetime import datetime
# import datetime
# from currency_converter import CurrencyConverter
# c = CurrencyConverter()
# from forex_python.converter import CurrencyRates
# c = CurrencyRates()
from py_currency_converter import convert

def normalize_data(df):
  return (df/df.loc[df.index[0],])*100

def fetch_date():
    date = datetime.now()
    dt = date.strftime('%Y-%m-%d')
    # Create a calendar
    nyse = mcal.get_calendar('NYSE')
    early = nyse.schedule(start_date=dt, end_date=dt)
    date_list = []
    list = mcal.date_range(early, frequency='1D')
    # print(list)
    for each in list:
        dt = each.strftime('%Y-%m-%d')
        date_list.append(dt)
    date_df = pd.DataFrame(date_list, columns =['date'])
    date_df.rename(columns = {'date':'Date'}, inplace = True)
    date_list = date_df.values.tolist()
    return(date_list)

def fetch_val(ticker):
    obj = stock_data.objects.all().filter(chart_type = ticker)
    for n in obj:
        data = n.current;
        # print(data)
    return(data)

def fetch_dt(ticker):
    try:
        co_obj = yf.Ticker(ticker)
        hist = co_obj.history(period="1d")
        hist.reset_index(inplace = True)
        data = hist["Date"]
        data = data.values.tolist()
        date = data[0]/1000000000
        # print(date)
        date = datetime.fromtimestamp(date).strftime('%m/%d/%Y')
        # print(date)
    except:
        print("no data")
        date = -1
    return(date)

def convert_data_eur(val):
    # val = float(val)
    val = convert(base='EUR', amount=val, to=['USD'])['USD']
    #val = temp['USD']
    val = round(val,2)
    return(val)

def convert_data_jpy(val):
    # val = float(val)
    val = convert(base='JPY', amount=val, to=['USD'])['USD']
    #val = temp['USD']
    val = round(val,2)
    return(val)

# fetch and store the hourly index data
@api_view(['GET'])
def pull_index_data_hourly(request):
    iom_index_hourly()
    smf_index_hourly()
    # f_index_hourly()
    pmf_index_hourly()
    return Response({"status":200})

def iom_index_hourly():
    try:
        # print("IOM")
        ticker_list = ["RIO","VALE","SXC","BHP"]
        dt = fetch_dt(ticker_list[0])
        # print(dt)
        result_list = [dt]
        if dt != -1:
            for each in ticker_list:
                result = fetch_val(each)
                result_list.append(round(result,2))
            print(result_list)
            first_list = [59.89, 13.45, 6.18, 54.92]
            sec_list = [result_list[1],result_list[2],result_list[3],result_list[4]]
            temp_list = []
            temp_list.append(first_list)
            temp_list.append(sec_list)
            df = pd.DataFrame(temp_list)
            df_pipe_normalized = normalize_data(df)
            df_mean = df_pipe_normalized.mean(axis=1)
            val_list = df_mean.tolist()
            val = val_list[1]
            data_save(val, dt,'iron ore mining')
            hourly_data_save(val, dt,'iron ore mining')
            obj = index_iom_data.objects.all().order_by('-id')[:2]
            # print(obj)
            for each in obj:
                if dt != each.date:
                    pre_val = each.IOM_index
                    # print(pre_val)
                    break
            stock_diff(val, pre_val, 'iron_ore')
            insert_updated_time('iron_ore')

    except Exception as e:
        err = "Error: " + str(e)
        url = "http://localhost:8000/texisle-app/send_mail/"
        payload={'content': 'Issue with hourly IOM index data pull\n'+ err}
        response = requests.request("POST", url, headers={}, data=payload, files={})

def f_index_hourly():
    try:
        # print("F")
        ticker_list = ["HO=F","RB=F"]
        dt = fetch_dt(ticker_list[0])
        result_list = [dt]
        if dt != -1:
            for each in ticker_list:
                result = fetch_val(each)
                result_list.append(round(result,2))
            # print(result_list)
            first_list = [2.02, 1.7]
            sec_list = [result_list[1],result_list[2]]
            temp_list = []
            temp_list.append(first_list)
            temp_list.append(sec_list)
            df = pd.DataFrame(temp_list)
            df_pipe_normalized = normalize_data(df)
            df_mean = df_pipe_normalized.mean(axis=1)
            val_list = df_mean.tolist()
            val = val_list[1]
            data_save(val, dt,'fuel')
            obj= index_f_data.objects.latest('id')
            pre_val = obj.F_index
            stock_diff(val, pre_val, 'fuel')
            insert_updated_time('fuel')
    except:
        url = "http://localhost:8000/texisle-app/send_mail/"
        payload={'content': 'Issue with hourly Fuel index data pull'}
        response = requests.request("POST", url, headers={}, data=payload, files={})

def pmf_index_hourly():
    try:
        # print("PMF")
        ticker_list = ["TS","VK.PA","X","TMST","NWPX"]
        dt = fetch_dt(ticker_list[0])
        result_list = [dt]
        if dt != -1:
            for each in ticker_list:
                result = fetch_val(each)
                result_list.append(round(result,2))
            # result_list[2] = convert_data_eur(result_list[2])
            print(result_list)
            first_list = [22.62,112.16,10.82,7.73,33.17]
            sec_list = [result_list[1],result_list[2],result_list[3],result_list[4],result_list[5]]
            temp_list = []
            temp_list.append(first_list)
            temp_list.append(sec_list)
            df = pd.DataFrame(temp_list)
            df_pipe_normalized = normalize_data(df)
            df_mean = df_pipe_normalized.mean(axis=1)
            val_list = df_mean.tolist()
            val = val_list[1]
            data_save(val, dt,'pipe manufacturing')
            hourly_data_save(val, dt,'pipe manufacturing')
            # obj= index_pmf_data.objects.latest('id')
            obj = index_pmf_data.objects.all().order_by('-id')[:2]
            # print(obj)
            for each in obj:
                if dt != each.date:
                    pre_val = each.PMF_index
                    # print(pre_val)
                    break
            stock_diff(val, pre_val, 'pipe_manufacturing')
            insert_updated_time('pipe_manufacturing')
    except Exception as e:
        err = "Error: " + str(e)
        url = "http://localhost:8000/texisle-app/send_mail/"
        payload={'content': 'Issue with hourly PMF index data pull\n'+ err}
        response = requests.request("POST", url, headers={}, data=payload, files={})

def smf_index_hourly():
    try:
        # print("SMF")
        ticker_list = ["MT","PKX","NUE","STLD","RS","CLF","TX","GGB","X","CMC","TKA.DE","SZG.DE","5401.T","5411.T"]
        dt = fetch_dt(ticker_list[0])
        result_list = [dt]
        if dt != -1:
            for each in ticker_list:
                result = fetch_val(each)
                result_list.append(round(result,2))
            # result_list[11] = convert_data_eur(result_list[11])
            # result_list[12] = convert_data_eur(result_list[12])
            # result_list[13] = convert_data_jpy(result_list[13])
            # result_list[14] = convert_data_jpy(result_list[14])
            print(result_list)
            first_list = [17.71, 51.21, 55.12, 33.8, 119.25, 7.84, 22.72, 5.09, 10.82, 22.35, 14.19, 23.28, 14.15, 12.02]
            sec_list = [result_list[1],result_list[2],result_list[3],result_list[4],result_list[5],result_list[6],result_list[7],result_list[8],result_list[9],result_list[10],result_list[11],result_list[12],result_list[13],result_list[14]]
            temp_list = []
            temp_list.append(first_list)
            temp_list.append(sec_list)
            df = pd.DataFrame(temp_list)
            df_pipe_normalized = normalize_data(df)
            df_mean = df_pipe_normalized.mean(axis=1)
            val_list = df_mean.tolist()
            val = val_list[1]
            data_save(val, dt,'steel manufacturing')
            hourly_data_save(val, dt,'steel manufacturing')
            # obj= index_smf_data.objects.latest('id')
            obj = index_smf_data.objects.all().order_by('-id')[:2]
            # print(obj)
            for each in obj:
                if dt != each.date:
                    pre_val = each.SMF_index
                    # print(pre_val)
                    break
            stock_diff(val, pre_val, 'steel_manufacturing')
            insert_updated_time('steel_manufacturing')
    except Exception as e:
        err = "Error: " + str(e)
        url = "http://localhost:8000/texisle-app/send_mail/"    
        payload={'content': 'Issue with hourly SMF index data pull\n'+ err}
        response = requests.request("POST", url, headers={}, data=payload, files={})

def data_save(val, date,chart_type):
    dt = datetime.now()
    if val>0:
        try:
            a = daily_index.objects.get(chart = chart_type)
            a.date = date
            a.val = round(val,2)
            a.update_time = dt
            a.save()
        except:
            data_obj = daily_index(date = date, val = round(val,2), chart = chart_type, update_time = dt)
            data_obj.save()

def hourly_data_save(val, date,chart_type):
    dt = datetime.now()
    if val>0:
        data_obj = hourly_index(date = date, val = round(val,2), chart = chart_type, update_time = dt)
        data_obj.save()

# update the stock data table
def stock_diff(val, pre_val, chart_type):
    if val>0:
        val = float(val)
        pre_val = float(pre_val)
        diff = (val - pre_val)
        diff_per = round(((diff/pre_val)*100), 2)
        # print(diff_per)
        # stock_data.objects.filter(chart_type = chart_type).delete()
        # data_obj = stock_data(chart_type = chart_type , data = diff_per, current = round(val,2))
        data_obj = stock_data.objects.get(chart_type = chart_type)
        data_obj.data = diff_per
        data_obj.current = round(val,2)
        data_obj.save()
        print(chart_type, "stock data done")

# update the last updated time
def insert_updated_time(comp):
    dt = datetime.now(tz=timezone.utc)
    try:
        a = updated_time.objects.get(chart = comp)
        a.update_time = dt
        a.save()
    except:
        data_obj = updated_time(chart = comp, update_time = dt)
        data_obj.save()