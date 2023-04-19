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

@api_view(['GET'])
def fetch_rig_data(request):

    endpoint = fetch_link()

    # fetches the xlsb file and coverts the equired sheet into csv
    urllib.request.urlretrieve("https://bakerhughesrigcount.gcs-web.com"+endpoint, file_dir +"/downloads/file.xlsb")
    read_file = pd.read_excel (file_dir +'/downloads/file.xlsb', sheet_name='Current Weekly Summary')
    read_file.to_csv (file_dir +'/downloads/new_file.csv', index = None, header=True)

    df = pd.read_csv(file_dir +'/downloads/new_file.csv')
    data =[]
    for x in range(-13,0):
        data.append(df['Unnamed: 3'].iloc[x])
    data.append(df['Unnamed: 3'].iloc[11])
    insert_data(data)
    insert_updated_time("rig_count")

    return Response({"status":200})

# fetches the endpoint of the required xlb file from bakerhughes website
def fetch_link():
    URL = "https://bakerhughesrigcount.gcs-web.com/na-rig-count"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    quotes = []  # a list to store quotes
    quote = {}
    table = soup.find('table', attrs={'class': 'nirtable'})
    # print(table)
    for row in table.findAll('span', attrs={'class': 'file file--mime-application-vnd-ms-excel-sheet-binary-macroEnabled-12 file--general'}):
        quote['url'] = row.a['href']
        quotes.append(quote)
        break
    # print(quotes)
    return(quotes[0]['url'])

def insert_data(data):
    date_list = fetch_last_friday()
    dt = date_list[0][0]
    dt = datetime.strptime(dt, '%Y-%m-%d')
    date = dt.strftime('%m/%d/%Y')
    for x in range(0, len(data)):
        data[x] = float(data[x])
    data_obj = index_rig_data(date = date,Ardmore = data[0],Arkoma = data[1] , Barnett = data[2] , Cana = data[3] , Niobrara = data[4] , Ford = data[5] , Granite = data[6] , Haynesville = data[7] , Marcellus = data[8] , Mississippian = data[9] , Permian = data[10] , Utica = data[11] , Williston = data[12] , RC_index = data[13])
    data_obj.save()
    update_stock_value(data)

def update_stock_value(data):
    chart_list = ['Ardmore', 'Arkoma', 'Barnett', 'Cana', 'Niobrara', 'Ford', 'Granite', 'Haynesville', 'Marcellus', 'Mississippian', 'Permian', 'Utica', 'Williston', 'rc_index']
    print(data)
    for x in range(0, len(data)):
        val1 = float(data[x])
        data_obj = stock_data.objects.get(chart_type = chart_list[x])
        val2 = float(data_obj.current)
        diff = (val1 - val2)
        diff_per = round(((diff/val2)*100), 2)
        data_obj.current = val1
        data_obj.data = diff #diff_per
        data_obj.save()
        
def insert_updated_time(comp):
    dt = datetime.now(tz=timezone.utc)
    try:
        a = updated_time.objects.get(chart = comp)
        a.update_time = dt
        a.save()
    except:
        data_obj = updated_time(chart = comp, update_time = dt)
        data_obj.save()

def fetch_last_friday():
    date = datetime.now() + relativedelta(weekday=FR(-1))
    dt = date.strftime('%Y-%m-%d')
    # Create a calendar
    nyse = mcal.get_calendar('NYSE')
    early = nyse.schedule(start_date=dt, end_date=dt)
    date_list = []
    list = mcal.date_range(early, frequency='1D')
    print(list)
    for each in list:
        dt = each.strftime('%Y-%m-%d')
        date_list.append(dt)
    date_df = pd.DataFrame(date_list, columns =['date'])
    date_df.rename(columns = {'date':'Date'}, inplace = True)
    date_list = date_df.values.tolist()
    
    return(date_list)

