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
from numpy import ERR_CALL
import pandas_market_calendars as mcal
from datetime import datetime, timedelta, date
import yfinance as yf
import pandas as pd
import numpy as np
import time, os
from datetime import datetime
from datetime import datetime, timedelta, date
# from currency_converter import CurrencyConverter
# c = CurrencyConverter()
# from forex_python.converter import CurrencyRates
# c = CurrencyRates()
from py_currency_converter import convert

def normalize_data(df):
  return (df/df.loc[df.index[0],])*100


# fetch and store the index data daily
@api_view(['GET'])
def pull_index_data(request):
    iom_data()
    smf_data()
    f_data()
    pmf_data()
    # t_index_data()
    return Response({"status":200})

def fetch_date():
    presentday = datetime.now()
    date = presentday - timedelta(days = 1)
    # date = presentday - timedelta(days = 3)
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

def fetch_date_rmi(num):
    presentday = datetime.now()
    date = presentday - timedelta(days = num)
    # date = presentday - timedelta(days = 3)
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

def fetch_val(date, ticker):
    try:
        print(date, ticker)
        hist = yf.download(ticker, start=date)
        hist.reset_index(inplace = True)
        hist.rename(columns = {'Close':ticker}, inplace = True)
        data = hist[ticker]
        data = data.values.tolist()
        data = data[0]
    except:
        print("no data")
        data = -9
    return(data)

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

# Iron Ore Mining Data
def iom_data():
    try:
        date_list = fetch_date()
        date_len = len(date_list)
        if date_len!=0:
            date = date_list[0][0]
            print("Pulling data for ", date)
            result_list = [date]
            ticker_list = ["RIO","VALE","SXC","BHP"]
            for each in ticker_list:
                result = fetch_val(date, each)
                result_list.append(round(result,2))
            dt = datetime.strptime(result_list[0], '%Y-%m-%d')
            result_list[0] = dt.strftime('%m/%d/%Y')

            print(result_list)
            try:
                temp = result_list[1:]
                # temp.pop(0)
                print(result_list)
                print(temp)
                for each in temp:
                    print(int(each))
                print("No null value present")
                data_obj = index_iom_data(date = result_list[0], RIO = result_list[1], VALE = result_list[2], SXC = result_list[3], BHP = result_list[4])
                data_obj.save()
                iom_index_calc()
                insert_updated_time('iron_ore')
            except:
                print("null value present")
                time.sleep(60)
                iom_data()
            print(result_list)
        else:
            print("No data to be pulled")
    except Exception as e:
        err = "Error: " + str(e)
        url = "http://localhost:8000/texisle-app/send_mail/"
        payload={'content': 'Issue with daily IOM index data pull\n'+ err}
        response = requests.request("POST", url, headers={}, data=payload, files={})
    
def iom_index_calc():
    index_list = ['RIO','VALE','SXC','BHP']
    index_obj = index_iom_data.objects.all()
    df = read_frame(index_obj, fieldnames=['RIO','VALE','SXC','BHP'])
    date_df = read_frame(index_obj, fieldnames=['date'])
    for index in index_list:
        df[[index]] = df[[index]].apply(pd.to_numeric)
    df_pipe_normalized = normalize_data(df)
    df_mean = df_pipe_normalized.mean(axis=1)
    final_df = pd.concat([date_df, df_mean], axis=1)
    # print(final_df)
    df_list = final_df.values.tolist()
    data = df_list[-1]
    print(data)
    a = index_iom_data.objects.get(date=data[0])
    a.IOM_index = data[1]
    a.save()
    val1 = df_list[-1][1]
    val2 = df_list[-2][1]
    diff = val1 - val2
    diff_per = round(((diff/val2)*100), 2)
    stock_data.objects.filter(chart_type = 'iron_ore').delete()
    data_obj = stock_data(chart_type = 'iron_ore' , data = diff_per, current = round(val1,2))
    data_obj.save()

# Fuel Data
def f_data():
    try:
        date_list = fetch_date()
        date_len = len(date_list)
        if date_len!=0:
            date = date_list[0][0]
            print("Pulling data for ", date)
            result_list = [date]
            ticker_list = ["HO=F","RB=F"]
            for each in ticker_list:
                result = fetch_val(date, each)
                result_list.append(round(result,2))
            dt = datetime.strptime(result_list[0], '%Y-%m-%d')
            result_list[0] = dt.strftime('%m/%d/%Y')
            print(result_list)
            data_obj = index_f_data(date = result_list[0], HO = result_list[1], RB = result_list[2])
            data_obj.save()
            f_index_calc()
            insert_updated_time('fuel')
        else:
            print("No data to be pulled")
    except:
        url = "http://localhost:8000/texisle-app/send_mail/"
        payload={'content': 'Issue with daily fuel index data pull'}
        response = requests.request("POST", url, headers={}, data=payload, files={})

def f_index_calc():
    index_list = ["HO","RB"]
    index_obj = index_f_data.objects.all()
    df = read_frame(index_obj, fieldnames=["HO","RB"])
    date_df = read_frame(index_obj, fieldnames=['date'])
    for index in index_list:
        df[[index]] = df[[index]].apply(pd.to_numeric)
    df_pipe_normalized = normalize_data(df)
    df_mean = df_pipe_normalized.mean(axis=1)
    final_df = pd.concat([date_df, df_mean], axis=1)
    # print(final_df)
    df_list = final_df.values.tolist()
    data = df_list[-1]
    print(data)
    a = index_f_data.objects.get(date=data[0])
    a.F_index = data[1]
    a.save()
    val1 = df_list[-1][1]
    val2 = df_list[-2][1]
    diff = val1 - val2
    diff_per = round(((diff/val2)*100), 2)
    stock_data.objects.filter(chart_type = 'fuel').delete()
    data_obj = stock_data(chart_type = 'fuel' , data = diff_per, current = round(val1,2))
    data_obj.save()

# Pipe Manufacturing Data
def pmf_data():
    try:
        date_list = fetch_date()
        date_len = len(date_list)
        if date_len!=0:
            date = date_list[0][0]
            print("Pulling data for ", date)
            result_list = [date]
            ticker_list = ["TS","VK.PA","X","TMST","NWPX"]
            for each in ticker_list:
                result = fetch_val(date, each)
                result_list.append(round(result,2))
            dt = datetime.strptime(result_list[0], '%Y-%m-%d')
            result_list[0] = dt.strftime('%m/%d/%Y')

            print(result_list)
            try:
                temp = result_list[1:]
                # temp.pop(0)
                print(temp)
                for each in temp:
                    print(int(each))
                print("No null value present")
                result_list[2] = convert_data_eur(result_list[2])
                data_obj = index_pmf_data(date = result_list[0], TS = result_list[1], VKPA = result_list[2], X = result_list[3], TMST = result_list[4], NWPX = result_list[5])
                data_obj.save()
                pmf_index_calc()
                insert_updated_time('pipe_manufacturing')
            except:
                print("null value present")
                time.sleep(60)
                pmf_data()

        else:
            print("No data to be pulled")
    except Exception as e:
        err = "Error: " + str(e)
        url = "http://localhost:8000/texisle-app/send_mail/"
        payload={'content': 'Issue with daily PMF index data pull\n'+ err}
        response = requests.request("POST", url, headers={}, data=payload, files={})

def pmf_index_calc():
    index_list = ["TS","VKPA","X","TMST","NWPX"]
    index_obj = index_pmf_data.objects.all()
    df = read_frame(index_obj, fieldnames=["TS","VKPA","X","TMST","NWPX"])
    date_df = read_frame(index_obj, fieldnames=['date'])
    for index in index_list:
        df[[index]] = df[[index]].apply(pd.to_numeric)
    df_pipe_normalized = normalize_data(df)
    df_mean = df_pipe_normalized.mean(axis=1)
    final_df = pd.concat([date_df, df_mean], axis=1)
    # print(final_df)
    df_list = final_df.values.tolist()
    data = df_list[-1]
    print(data)
    a = index_pmf_data.objects.get(date=data[0])
    a.PMF_index = data[1]
    a.save()
    val1 = df_list[-1][1]
    val2 = df_list[-2][1]
    diff = val1 - val2
    diff_per = round(((diff/val2)*100), 2)
    stock_data.objects.filter(chart_type = 'pipe_manufacturing').delete()
    data_obj = stock_data(chart_type = 'pipe_manufacturing' , data = diff_per, current = round(val1,2))
    data_obj.save()

# Steel market manufacturing Data
def smf_data():
    try:
        date_list = fetch_date()
        date_len = len(date_list)
        if date_len!=0:
            date = date_list[0][0]
            print("Pulling data for ", date)
            result_list = [date]
            ticker_list = ["MT","PKX","NUE","STLD","RS","CLF","TX","GGB","X","CMC","TKA.DE","SZG.DE","5401.T","5411.T"]
            for each in ticker_list:
                result = fetch_val(date, each)
                result_list.append(round(result,2))
            dt = datetime.strptime(result_list[0], '%Y-%m-%d')
            result_list[0] = dt.strftime('%m/%d/%Y')
            result_list[11] = convert_data_eur(result_list[11])
            result_list[12] = convert_data_eur(result_list[12])
            result_list[13] = convert_data_jpy(result_list[13])
            result_list[14] = convert_data_jpy(result_list[14])

            print(result_list)
            try:
                temp = result_list[1:]
                # temp.pop(0)
                print(temp)
                for each in temp:
                    print(int(each))
                print("No null value present")
                data_obj = index_smf_data(date = result_list[0], MT = result_list[1], PKX = result_list[2], NUE = result_list[3], STLD = result_list[4], RS = result_list[5], CLF = result_list[6], TX = result_list[7], GGB = result_list[8], X = result_list[9], CMC = result_list[10], TKADE = result_list[11], SZGDE = result_list[12], NIPPON = result_list[13], JFE = result_list[14])
                data_obj.save()
                smf_index_calc()
                insert_updated_time('steel_manufacturing')
            except:
                print("null value present")
                time.sleep(60)
                smf_data()
        else:
            print("No data to be pulled")
    except Exception as e:
        err = "Error: " + str(e)
        url = "http://localhost:8000/texisle-app/send_mail/"
        payload={'content': 'Issue with daily SMF index data pull\n'+ err}
        response = requests.request("POST", url, headers={}, data=payload, files={})

def smf_index_calc():
    index_list = ["MT","PKX","NUE","STLD","RS","CLF","TX","GGB","X","CMC","TKADE","SZGDE","NIPPON","JFE"]
    index_obj = index_smf_data.objects.all()
    df = read_frame(index_obj, fieldnames=["MT","PKX","NUE","STLD","RS","CLF","TX","GGB","X","CMC","TKADE","SZGDE","NIPPON","JFE"])
    date_df = read_frame(index_obj, fieldnames=['date'])
    for index in index_list:
        df[[index]] = df[[index]].apply(pd.to_numeric)
    df_pipe_normalized = normalize_data(df)
    df_mean = df_pipe_normalized.mean(axis=1)
    final_df = pd.concat([date_df, df_mean], axis=1)
    # print(final_df)
    df_list = final_df.values.tolist()
    data = df_list[-1]
    print(data)
    a = index_smf_data.objects.get(date=data[0])
    a.SMF_index = data[1]
    a.save()
    val1 = df_list[-1][1]
    val2 = df_list[-2][1]
    diff = val1 - val2
    diff_per = round(((diff/val2)*100), 2)
    stock_data.objects.filter(chart_type = 'steel_manufacturing').delete()
    data_obj = stock_data(chart_type = 'steel_manufacturing' , data = diff_per, current = round(val1,2))
    data_obj.save()

#save updated time
def insert_updated_time(comp):
    dt = datetime.now(tz=timezone.utc)
    try:
        a = updated_time.objects.get(chart = comp)
        a.update_time = dt
        a.save()
    except:
        data_obj = updated_time(chart = comp, update_time = dt)
        data_obj.save()

#Raw Material Data
@api_view(['GET'])
def rmi_index_cme(request):
    try:
        # get last working day
        day = datetime.today().weekday()
        if day==0:
            date_list = fetch_date_rmi(3)
        else:
            date_list = fetch_date_rmi(1)
        date_len = len(date_list)
        if date_len!=0:
            date = date_list[0][0]
            dt = datetime.strptime(date, '%Y-%m-%d')
            date = dt.strftime('%m-%d-%Y')
            date_y = dt.strftime('%m/%d/%Y')
            print("Pulling data for ", date)
            result_list = [date_y]
            # fetch last available data for scrap
            scrap_obj = rmi_data.objects.values('data').filter(chart = "Scrap", date = date)[0]
            result_list.append(scrap_obj['data'])
            print("scrap")
            # fetch last available data for hrc
            hrc_obj = rmi_data.objects.values('data').filter(chart = "HRC", date = date)[0]
            result_list.append(hrc_obj['data'])
            print("hrc")
            # fetch last available data for coal
            yahoo_obj = yahoo_data.objects.values('data').filter(chart="MFFH22.NYM", chart_type = "1week", date = date)[0]
            result_list.append(yahoo_obj['data'])
            print("coal")
            # fetch last available data for iron
            iron_obj = rmi_data.objects.values('data').filter(chart = "Iron", date = date)[0]
            result_list.append(iron_obj['data'])
            print("iron")
            print(result_list)
            data_obj = index_rmi_cme_data(date = result_list[0], SCRAP = result_list[1], HRC = result_list[2], COAL = result_list[3], IRONORE = result_list[4])
            data_obj.save()
            rmi_index_cme_calc()
            insert_updated_time('raw_material_index')
        return Response({"status":200})
    except Exception as e:
        err = "Error: " + str(e)
        # print("oops")
        url = "http://localhost:8000/texisle-app/send_mail/"
        payload={'content': 'Issue with daily RMI index CME data pull\n'+ err}
        response = requests.request("POST", url, headers={}, data=payload, files={})
        return Response({"status":500})
    
def rmi_index_cme_calc():
    index_list = ["SCRAP","HRC","COAL","IRONORE"]
    index_obj = index_rmi_cme_data.objects.all()
    df = read_frame(index_obj, fieldnames=["SCRAP","HRC","COAL","IRONORE"])
    date_df = read_frame(index_obj, fieldnames=['date'])
    for index in index_list:
        df[[index]] = df[[index]].apply(pd.to_numeric)
    df_pipe_normalized = normalize_data(df)
    df_mean = df_pipe_normalized.mean(axis=1)
    final_df = pd.concat([date_df, df_mean], axis=1)
    print(final_df)
    df_list = final_df.values.tolist()
    data = df_list[-1]
    print(data)
    # for each in df_list:
    a = index_rmi_cme_data.objects.get(date=data[0])
    a.RMI_index = data[1]
    a.save()
    val1 = df_list[-1][1]
    val2 = df_list[-2][1]
    diff = val1 - val2
    diff_per = round(((diff/val2)*100), 2)
    stock_data.objects.filter(chart_type = 'raw_material_index').delete()
    data_obj = stock_data(chart_type = 'raw_material_index' , data = diff_per, current = round(val1,2))
    data_obj.save()

#Transportation Data
@api_view(['GET'])
def t_index_data(request):
    try:
        # last working day
        day = datetime.today().weekday()
        if day==0:
            date_list = fetch_date_rmi(3)
        else:
            date_list = fetch_date_rmi(1)
        date_len = len(date_list)
        if date_len!=0:
            date = date_list[0][0]
            dt = datetime.strptime(date, '%Y-%m-%d')
            date = dt.strftime('%m-%d-%Y')
            date_y = dt.strftime('%m/%d/%Y')
            print("Pulling data for ", date)
            result_list = [date_y]
            # fetch last available data for ULSD
            ulsd_obj = transportation_data.objects.values('data').filter(chart = "ULSD", date = date)[0]
            result_list.append(ulsd_obj['data'])
            print("ulsd")
            # fetch last available data for BADI
            baltic_obj = transportation_data.objects.values('data').filter(chart = "Baltic", date = date)[0]
            result_list.append(baltic_obj['data'])
            print("baltic")
            # fetch last available data for AllGrades
            ag_obj = transportation_data.objects.filter(chart = "All-Grade").last()
            print(ag_obj.data)
            result_list.append(ag_obj.data)
            print("all grade")
            print(result_list)
            data_obj = index_t_data(date = result_list[0], ULSD = result_list[1], BALTIC = result_list[2], ALLGRADE = result_list[3])
            data_obj.save()
            t_index_calc()
            insert_updated_time('transportation')
        return Response({"status":200})
    except Exception as e:
        err = "Error: " + str(e)
        print(err)
        url = "http://localhost:8000/texisle-app/send_mail/"
        payload={'content': 'Issue with daily transport index CME data pull\n'+ err}
        response = requests.request("POST", url, headers={}, data=payload, files={})
        return Response({"status":500})
    
def t_index_calc():
    index_list = ["ULSD","BALTIC","ALLGRADE"]
    index_obj = index_t_data.objects.all()
    df = read_frame(index_obj, fieldnames=["ULSD","BALTIC","ALLGRADE"])
    date_df = read_frame(index_obj, fieldnames=['date'])
    for index in index_list:
        df[[index]] = df[[index]].apply(pd.to_numeric)
    df_pipe_normalized = normalize_data(df)
    df_mean = df_pipe_normalized.mean(axis=1)
    final_df = pd.concat([date_df, df_mean], axis=1)
    # print(final_df)
    df_list = final_df.values.tolist()
    data = df_list[-5:]
    # print(data)
    for each in data:
        print(each)
        a = index_t_data.objects.get(date=each[0])
        a.T_index = each[1]
        a.save()
    val1 = df_list[-1][1]
    val2 = df_list[-2][1]
    diff = val1 - val2
    diff_per = round(((diff/val2)*100), 2)
    stock_data.objects.filter(chart_type = 'transport').delete()
    data_obj = stock_data(chart_type = 'transport' , data = diff_per, current = round(val1,2))
    data_obj.save()