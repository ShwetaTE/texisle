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
from dateutil.relativedelta import relativedelta, FR
# import datetime
import requests
import json
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
# file_dir = os.path.dirname(__file__)+"."

def insert_updated_time(comp):
    dt = datetime.now(tz=timezone.utc)
    try:
        a = updated_time.objects.get(chart = comp)
        a.update_time = dt
        a.save()
    except:
        data_obj = updated_time(chart = comp, update_time = dt)
        data_obj.save()

@api_view(['GET'])
def fetch_duc_data(request):
    # fetches the xlsb file and coverts the equired sheet into csv
    urllib.request.urlretrieve("https://www.eia.gov/petroleum/drilling/xls/duc-data.xlsx", file_dir +"/downloads/duc/duc-data.xlsx")
    read_file = pd.read_excel (file_dir +'/downloads/duc/duc-data.xlsx', sheet_name='Data')
    read_file.to_csv (file_dir +'/downloads/duc/duc-data.csv', index = None, header=True)
    duc_df = pd.read_csv(file_dir +'/downloads/duc/duc-data.csv')
    len = duc_df.shape[0]
    for each in range(4,len):
        duc_list = duc_df.iloc[each].tolist()
        date = duc_list[0]
        del duc_list[0]
        duc_list = [x for x in duc_list if str(x) != 'nan']
        date = date[:10]
        dt = datetime.strptime(date, '%Y-%m-%d')
        date = dt.strftime('%m/%d/%Y')
        # print(date)
        # print(duc_list)
        replace_data(date, duc_list)

    duc_list_1 = clean_data(duc_df.iloc[-2].tolist())
    duc_list_2 = clean_data(duc_df.iloc[-1].tolist())

    update_stock_value(duc_list_1, duc_list_2)

    return Response({"status":200})

def clean_data(data):
    date = data[0]
    del data[0]
    data = [x for x in data if str(x) != 'nan']
    date = date[:10]
    dt = datetime.strptime(date, '%Y-%m-%d')
    date = dt.strftime('%m/%d/%Y')
    temp_list = data[2:]
    data = temp_list[::3]
    return data

def replace_data(date, data):
    try:
        # print("date....",date)
        data_obj = index_duc_data.objects.get(date = date)
        # print(data_obj.Anadarko_DUC)
        data_obj.Anadarko_D = data[0]
        data_obj.Anadarko_C = data[1]
        data_obj.Anadarko_DUC = data[2]
        data_obj.Appalachia_D = data[3]
        data_obj.Appalachia_C = data[4]
        data_obj.Appalachia_DUC = data[5]
        data_obj.Bakken_D = data[6]
        data_obj.Bakken_C = data[7]
        data_obj.Bakken_DUC = data[8]
        data_obj.Eagle_D = data[9]
        data_obj.Eagle_C = data[10]
        data_obj.Eagle_DUC = data[11]
        data_obj.Haynesville_D = data[12]
        data_obj.Haynesville_C = data[13]
        data_obj.Haynesville_DUC = data[14]
        data_obj.Niobrara_D = data[15]
        data_obj.Niobrara_C = data[16]
        data_obj.Niobrara_DUC = data[17]
        data_obj.Permian_D = data[18]
        data_obj.Permian_C = data[19]
        data_obj.Permian_DUC = data[20]
        data_obj.DPR_D = data[21]
        data_obj.DPR_C = data[22]
        data_obj.DPR_DUC = data[23]
        data_obj.save()
    except:
        # print("except....",date)
        data_obj = index_duc_data(date = date, Anadarko_D = data[0], Anadarko_C = data[1], Anadarko_DUC = data[2], Appalachia_D = data[3], Appalachia_C = data[4], Appalachia_DUC = data[5], Bakken_D = data[6], Bakken_C = data[7], Bakken_DUC = data[8], Eagle_D = data[9], Eagle_C = data[10], Eagle_DUC = data[11], Haynesville_D = data[12], Haynesville_C = data[13], Haynesville_DUC = data[14], Niobrara_D = data[15], Niobrara_C = data[16], Niobrara_DUC = data[17], Permian_D = data[18], Permian_C = data[19], Permian_DUC = data[20], DPR_D = data[21], DPR_C = data[22], DPR_DUC = data[23] )
        data_obj.save()
        insert_updated_time("well_count")

def update_stock_value(duc_list_1, duc_list_2):
    # print(duc_list_1, duc_list_2)
    chart_list = ['Anadarko_DUC', 'Appalachia_DUC', 'Bakken_DUC', 'Eagle_DUC', 'Haynesville_DUC', 'Niobrara_DUC', 'Permian_DUC', 'DPR_DUC' ]
    # # print(data)
    for x in range(0, len(duc_list_1)):
        val1 = float(duc_list_2[x])
        data_obj = stock_data.objects.get(chart_type = chart_list[x])
        val2 = float(duc_list_1[x])
        diff = (val1 - val2)
        data_obj.current = val1
        # data_obj.data = diff_per
        data_obj.data = diff #diff_per
        data_obj.save()

########################
# @api_view(['GET'])
# def fetch_duc_data(request):
#     # fetches the xlsb file and coverts the equired sheet into csv
#     urllib.request.urlretrieve("https://www.eia.gov/petroleum/drilling/xls/duc-data.xlsx", file_dir +"./downloads/duc/duc-data.xlsx")
#     read_file = pd.read_excel (file_dir +'./downloads/duc/duc-data.xlsx', sheet_name='Data')
#     read_file.to_csv (file_dir +'./downloads/duc/duc-data.csv', index = None, header=True)

#     duc_df = pd.read_csv(file_dir +'./downloads/duc/duc-data.csv')
#     duc_list = duc_df.iloc[-1].tolist()
#     date = duc_list[0]
#     del duc_list[0]
#     data = [x for x in duc_list if str(x) != 'nan']

#     date = date[:10]
#     dt = datetime.strptime(date, '%Y-%m-%d')
#     date = dt.strftime('%m/%d/%Y')

#     data_obj = index_duc_data(date = date, Anadarko_D = data[0], Anadarko_C = data[1], Anadarko_DUC = data[2], Appalachia_D = data[3], Appalachia_C = data[4], Appalachia_DUC = data[5], Bakken_D = data[6], Bakken_C = data[7], Bakken_DUC = data[8], Eagle_D = data[9], Eagle_C = data[10], Eagle_DUC = data[11], Haynesville_D = data[12], Haynesville_C = data[13], Haynesville_DUC = data[14], Niobrara_D = data[15], Niobrara_C = data[16], Niobrara_DUC = data[17], Permian_D = data[18], Permian_C = data[19], Permian_DUC = data[20], DPR_D = data[21], DPR_C = data[22], DPR_DUC = data[23] )
#     data_obj.save()
#     update_stock_value(data)
#     insert_updated_time("well_count")

#     return Response({"status":200})

# def update_stock_value(data):
#     temp_list = data[2:]
#     data = temp_list[::3]
#     chart_list = ['Anadarko_DUC', 'Appalachia_DUC', 'Bakken_DUC', 'Eagle_DUC', 'Haynesville_DUC', 'Niobrara_DUC', 'Permian_DUC', 'DPR_DUC' ]
#     # print(data)
#     for x in range(0, len(data)):
#         val1 = float(data[x])
#         data_obj = stock_data.objects.get(chart_type = chart_list[x])
#         val2 = float(data_obj.current)
#         diff = (val1 - val2)
#         diff_per = round(((diff/val2)*100), 2)
#         data_obj.current = val1
#         # data_obj.data = diff_per
#         data_obj.data = diff #diff_per
#         data_obj.save()
