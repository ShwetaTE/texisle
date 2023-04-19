from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
import json
from django.core import serializers
import time, os
from datetime import datetime
import requests

#using nodejs code
@csrf_exempt
@api_view(['GET'])
def data_pull(request):
    Scrap_data.objects.all().delete()
    print("started pulling scrap data...")
    scrap_data_pull()
    HRC_data.objects.all().delete()
    print("started pulling hrc data...")
    hrc_data_pull()
    print("started pulling stock data...")
    stock_data_pull()
    iron_data.objects.all().delete()
    print("started pulling iron data...")
    iron_data_pull()
    print("=================================")
    print("TURN OFF THE DATA LAKE!!!!!!!!!!")
    print("=================================")
    return Response({"status":200})

def scrap_data_pull():
    print("Started fetching data....")

    # url = "http://localhost:3000/Scrap/getData/default/"
    # headers = {'Content-Type': 'application/json'}
    # response = requests.request("GET", url, headers=headers, data={})
    # res = json.loads(response.text)
    # data = res["data"]
    # for n in data:
    #     # print(n[1])
    #     scrap_obj = Scrap_data(chart_type = 'default' , data = n[1], date = n[0])
    #     scrap_obj.save()
    # # time.sleep(15)
    # print("default done")

    # url = "http://localhost:3000/Scrap/getData/1day/"
    # headers = {'Content-Type': 'application/json'}
    # response = requests.request("GET", url, headers=headers, data={})
    # res = json.loads(response.text)
    # data = res["data"]
    # # print(data[1])
    # scrap_obj = Scrap_data(chart_type = '1day' , data = data[1], date = data[0])
    # scrap_obj.save()
    # # time.sleep(15)
    # print("1day done")

    url = "http://localhost:3000/Scrap/getData/1week/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={})
    res = json.loads(response.text)
    data = res["data"]
    for n in data:
        # print(n[1])
        dt = datetime.strptime(n[0], '%m/%d/%Y')
        n[0] = dt.strftime('%m/%d/%Y')
        scrap_obj = Scrap_data(chart_type = '1week' , data = float(n[1]), date = n[0])
        scrap_obj.save()
    # time.sleep(5)
    print("1week done")

    url = "http://localhost:3000/Scrap/getData/1month/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={})
    res = json.loads(response.text)
    data = res["data"]
    for n in data:
        # print(n[1])
        dt = datetime.strptime(n[0], '%m/%d/%Y')
        n[0] = dt.strftime('%m/%d/%Y')
        scrap_obj = Scrap_data(chart_type = '1month' , data = float(n[1]), date = n[0])
        scrap_obj.save()
    # time.sleep(15)
    print("1month done")

    url = "http://localhost:3000/Scrap/getData/3month/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={})
    res = json.loads(response.text)
    data = res["data"]
    for n in data:
        # print(n[1])
        dt = datetime.strptime(n[0], '%m/%d/%Y')
        n[0] = dt.strftime('%m/%d/%Y')
        scrap_obj = Scrap_data(chart_type = '3month' , data = float(n[1]), date = n[0])
        scrap_obj.save()
    # time.sleep(15)
    print("3month done")

    url = "http://localhost:3000/Scrap/getData/6month/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={})
    res = json.loads(response.text)
    data = res["data"]
    for n in data:
        # print(n[1])
        dt = datetime.strptime(n[0], '%m/%d/%Y')
        n[0] = dt.strftime('%m/%d/%Y')
        scrap_obj = Scrap_data(chart_type = '6month' , data = float(n[1]), date = n[0])
        scrap_obj.save()
    # time.sleep(15)
    print("6month done")

    url = "http://localhost:3000/Scrap/getData/1year/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={})
    res = json.loads(response.text)
    data = res["data"]
    for n in data:
        # print(n[1])
        dt = datetime.strptime(n[0], '%m/%d/%Y')
        n[0] = dt.strftime('%m/%d/%Y')
        scrap_obj = Scrap_data(chart_type = '1year' , data = float(n[1]), date = n[0])
        scrap_obj.save()
    # time.sleep(15)
    print("1 year done")

    url = "http://localhost:3000/Scrap/getData/2year/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={})
    res = json.loads(response.text)
    data = res["data"]
    for n in data:
        # print(n[1])
        dt = datetime.strptime(n[0], '%m/%d/%Y')
        n[0] = dt.strftime('%m/%d/%Y')
        scrap_obj = Scrap_data(chart_type = '2year' , data = float(n[1]), date = n[0])
        scrap_obj.save()
    # time.sleep(15)
    print("2 year done")

    return Response({"status":200})

def hrc_data_pull():
    print("Started fetching data....")

    # url = "http://localhost:3000/HRC/getData/default/"
    # headers = {'Content-Type': 'application/json'}
    # response = requests.request("GET", url, headers=headers, data={})
    # res = json.loads(response.text)
    # data = res["data"]
    # for n in data:
    #     # print(n[1])
    #     hrc_obj = HRC_data(chart_type = 'default' , data = n[1], date = n[0])
    #     hrc_obj.save()
    # # time.sleep(15)
    # print("default done")

    # url = "http://localhost:3000/HRC/getData/1day/"
    # headers = {'Content-Type': 'application/json'}
    # response = requests.request("GET", url, headers=headers, data={})
    # res = json.loads(response.text)
    # data = res["data"]
    # # print(data[1])
    # hrc_obj = HRC_data(chart_type = '1day' , data = data[1], date = data[0])
    # hrc_obj.save()
    # # time.sleep(15)
    # print("1day done")

    url = "http://localhost:3000/HRC/getData/1week/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={}, verify= False)
    res = json.loads(response.text)
    data = res["data"]
    for n in data:
        # print(n[1])
        dt = datetime.strptime(n[0], '%m/%d/%Y')
        n[0] = dt.strftime('%m/%d/%Y')
        hrc_obj = HRC_data(chart_type = '1week' , data = float(n[1]), date = n[0])
        hrc_obj.save()
    # time.sleep(5)
    print("1week done")

    url = "http://localhost:3000/HRC/getData/1month/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={}, verify= False)
    res = json.loads(response.text)
    data = res["data"]
    for n in data:
        # print(n[1])
        dt = datetime.strptime(n[0], '%m/%d/%Y')
        n[0] = dt.strftime('%m/%d/%Y')
        hrc_obj = HRC_data(chart_type = '1month' , data = float(n[1]), date = n[0])
        hrc_obj.save()
    # time.sleep(15)
    print("1month done")

    url = "http://localhost:3000/HRC/getData/3month/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={}, verify= False)
    res = json.loads(response.text)
    data = res["data"]
    for n in data:
        # print(n[1])
        dt = datetime.strptime(n[0], '%m/%d/%Y')
        n[0] = dt.strftime('%m/%d/%Y')
        hrc_obj = HRC_data(chart_type = '3month' , data = float(n[1]), date = n[0])
        hrc_obj.save()
    # time.sleep(15)
    print("3month done")

    url = "http://localhost:3000/HRC/getData/6month/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={}, verify= False)
    res = json.loads(response.text)
    data = res["data"]
    for n in data:
        # print(n[1])
        dt = datetime.strptime(n[0], '%m/%d/%Y')
        n[0] = dt.strftime('%m/%d/%Y')
        hrc_obj = HRC_data(chart_type = '6month' , data = float(n[1]), date = n[0])
        hrc_obj.save()
    # time.sleep(15)
    print("6month done")

    url = "http://localhost:3000/HRC/getData/1year/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={}, verify= False)
    res = json.loads(response.text)
    data = res["data"]
    for n in data:
        # print(n[1])
        dt = datetime.strptime(n[0], '%m/%d/%Y')
        n[0] = dt.strftime('%m/%d/%Y')
        hrc_obj = HRC_data(chart_type = '1year' , data = float(n[1]), date = n[0])
        hrc_obj.save()
    # time.sleep(15)
    print("1 year done")

    url = "http://localhost:3000/HRC/getData/2year/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={}, verify= False)
    res = json.loads(response.text)
    data = res["data"]
    for n in data:
        # print(n[1])
        dt = datetime.strptime(n[0], '%m/%d/%Y')
        n[0] = dt.strftime('%m/%d/%Y')
        hrc_obj = HRC_data(chart_type = '2year' , data = float(n[1]), date = n[0])
        hrc_obj.save()
    # time.sleep(15)
    print("2 year done")

    return Response({"status":200})

def iron_data_pull():
    print("Started fetching data....")

    url = "http://localhost:3000/IronOre/getData/1week/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={}, verify= False)
    res = json.loads(response.text)
    data = res["data"]
    for n in data:
        # print(n[1])
        dt = datetime.strptime(n[0], '%m/%d/%Y')
        n[0] = dt.strftime('%m/%d/%Y')
        hrc_obj = iron_data(chart_type = '1week' , data = float(n[1]), date = n[0])
        hrc_obj.save()
    # time.sleep(5)
    print("1week done")

    url = "http://localhost:3000/IronOre/getData/1month/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={}, verify= False)
    res = json.loads(response.text)
    data = res["data"]
    for n in data:
        # print(n[1])
        dt = datetime.strptime(n[0], '%m/%d/%Y')
        n[0] = dt.strftime('%m/%d/%Y')
        hrc_obj = iron_data(chart_type = '1month' , data = float(n[1]), date = n[0])
        hrc_obj.save()
    # time.sleep(15)
    print("1month done")

    url = "http://localhost:3000/IronOre/getData/3month/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={}, verify= False)
    res = json.loads(response.text)
    data = res["data"]
    for n in data:
        # print(n[1])
        dt = datetime.strptime(n[0], '%m/%d/%Y')
        n[0] = dt.strftime('%m/%d/%Y')
        hrc_obj = iron_data(chart_type = '3month' , data = float(n[1]), date = n[0])
        hrc_obj.save()
    # time.sleep(15)
    print("3month done")

    url = "http://localhost:3000/IronOre/getData/6month/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={}, verify= False)
    res = json.loads(response.text)
    data = res["data"]
    for n in data:
        # print(n[1])
        dt = datetime.strptime(n[0], '%m/%d/%Y')
        n[0] = dt.strftime('%m/%d/%Y')
        hrc_obj = iron_data(chart_type = '6month' , data = float(n[1]), date = n[0])
        hrc_obj.save()
    # time.sleep(15)
    print("6month done")

    url = "http://localhost:3000/IronOre/getData/1year/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={}, verify= False)
    res = json.loads(response.text)
    data = res["data"]
    for n in data:
        # print(n[1])
        dt = datetime.strptime(n[0], '%m/%d/%Y')
        n[0] = dt.strftime('%m/%d/%Y')
        hrc_obj = iron_data(chart_type = '1year' , data = float(n[1]), date = n[0])
        hrc_obj.save()
    # time.sleep(15)
    print("1 year done")

    url = "http://localhost:3000/IronOre/getData/2year/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={}, verify= False)
    res = json.loads(response.text)
    data = res["data"]
    for n in data:
        # print(n[1])
        dt = datetime.strptime(n[0], '%m/%d/%Y')
        n[0] = dt.strftime('%m/%d/%Y')
        hrc_obj = iron_data(chart_type = '2year' , data = float(n[1]), date = n[0])
        hrc_obj.save()
    # time.sleep(15)
    print("2 year done")

    return Response({"status":200})

def stock_data_pull():
    print("Started fetching data....")
    stock_data.objects.filter(chart_type = "scrap").delete()
    url = "http://localhost:3000/Scrap/getData/stockChange/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={})
    res = json.loads(response.text)
    scrap_data = res
    data_obj = stock_data(chart_type = 'scrap' , data = scrap_data["data"], current = scrap_data["current"])
    data_obj.save()
    print("Srap stock data done")

    stock_data.objects.filter(chart_type = "hrc").delete()
    url = "http://localhost:3000/HRC/getData/stockChange/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={})
    res = json.loads(response.text)
    hrc_data = res
    data_obj = stock_data(chart_type = 'hrc' , data = hrc_data["data"], current = hrc_data["current"])
    data_obj.save()
    print("HRC stock data done")

    stock_data.objects.filter(chart_type = "iron").delete()
    url = "http://localhost:3000/IronOre/getData/stockChange/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={})
    res = json.loads(response.text)
    iron_data = res
    data_obj = stock_data(chart_type = 'iron' , data = iron_data["data"], current = iron_data["current"])
    data_obj.save()
    print("iron stock data done")

    return Response({"status":200})


# API to pull perday data from dl using nodejs code
@api_view(['GET'])
def dl_data_pull(request):
    print("started pulling scrap data...")
    scrap()
    print("started pulling hrc data...")
    hrc()
    print("started pulling iron data...")
    ironore()
    print("started pulling stock data...")
    stock_data_pull()
    print("=================================")
    print("TURN OFF THE DATA LAKE!!!!!!!!!!")
    print("=================================")
    return Response({'status': 200})

def scrap():
    url = "http://localhost:3000/Scrap/getData/1week/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={})
    res = json.loads(response.text)
    # res = { "status": 200, "data": [ [ "12/29/2021", "118.3" ], [ "12/30/2021", "119.28" ], [ "12/31/2021", "120.75" ], [ "1/3/2022", "122.26" ], [ "1/4/2022", "123.12" ], [ "1/5/2022", "124.89" ] ] }
    data_list = res["data"]
    temp = data_list[-1]
    data = temp[1]
    dt = datetime.strptime(temp[0], '%m/%d/%Y')
    date = dt.strftime('%m/%d/%Y')

    scrap_obj = Scrap_data(chart_type = "1week" , data = data, date = date)
    scrap_obj.save()
    scrap_obj = Scrap_data(chart_type = "1month" , data = data, date = date)
    scrap_obj.save()
    scrap_obj = Scrap_data(chart_type = "3month" , data = data, date = date)
    scrap_obj.save()
    scrap_obj = Scrap_data(chart_type = "6month" , data = data, date = date)
    scrap_obj.save()
    scrap_obj = Scrap_data(chart_type = "1year" , data = data, date = date)
    scrap_obj.save()
    scrap_obj = Scrap_data(chart_type = "2year" , data = data, date = date)
    scrap_obj.save()

    scrap_obj = Scrap_data.objects.filter(chart_type = "1week").first()
    scrap_obj.delete()
    scrap_obj = Scrap_data.objects.filter(chart_type = "1month").first()
    scrap_obj.delete()
    scrap_obj = Scrap_data.objects.filter(chart_type = "3month").first()
    scrap_obj.delete()
    scrap_obj = Scrap_data.objects.filter(chart_type = "6month").first()
    scrap_obj.delete()
    scrap_obj = Scrap_data.objects.filter(chart_type = "1year").first()
    scrap_obj.delete()
    scrap_obj = Scrap_data.objects.filter(chart_type = "2year").first()
    scrap_obj.delete()
    return()

def hrc():
    url = "http://localhost:3000/HRC/getData/1week/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={})
    res = json.loads(response.text)
    # res = { "status": 200, "data": [ [ "12/29/2021", "118.3" ], [ "12/30/2021", "119.28" ], [ "12/31/2021", "120.75" ], [ "1/3/2022", "122.26" ], [ "1/4/2022", "123.12" ], [ "1/5/2022", "124.89" ] ] }
    data_list = res["data"]
    temp = data_list[-1]
    data = temp[1]
    dt = datetime.strptime(temp[0], '%m/%d/%Y')
    date = dt.strftime('%m/%d/%Y')

    hrc_obj = HRC_data(chart_type = "1week" , data = data, date = date)
    hrc_obj.save()
    hrc_obj = HRC_data(chart_type = "1month" , data = data, date = date)
    hrc_obj.save()
    hrc_obj = HRC_data(chart_type = "3month" , data = data, date = date)
    hrc_obj.save()
    hrc_obj = HRC_data(chart_type = "6month" , data = data, date = date)
    hrc_obj.save()
    hrc_obj = HRC_data(chart_type = "1year" , data = data, date = date)
    hrc_obj.save()
    hrc_obj = HRC_data(chart_type = "2year" , data = data, date = date)
    hrc_obj.save()

    hrc_obj = HRC_data.objects.filter(chart_type = "1week").first()
    hrc_obj.delete()
    hrc_obj = HRC_data.objects.filter(chart_type = "1month").first()
    hrc_obj.delete()
    hrc_obj = HRC_data.objects.filter(chart_type = "3month").first()
    hrc_obj.delete()
    hrc_obj = HRC_data.objects.filter(chart_type = "6month").first()
    hrc_obj.delete()
    hrc_obj = HRC_data.objects.filter(chart_type = "1year").first()
    hrc_obj.delete()
    hrc_obj = HRC_data.objects.filter(chart_type = "2year").first()
    hrc_obj.delete()
    return()

def ironore():
    url = "http://localhost:3000/IronOre/getData/1week/"
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data={})
    res = json.loads(response.text)
    # res = { "status": 200, "data": [ [ "12/29/2021", "118.3" ], [ "12/30/2021", "119.28" ], [ "12/31/2021", "120.75" ], [ "1/3/2022", "122.26" ], [ "1/4/2022", "123.12" ], [ "1/5/2022", "124.89" ] ] }
    data_list = res["data"]
    temp = data_list[-1]
    data = temp[1]
    dt = datetime.strptime(temp[0], '%m/%d/%Y')
    date = dt.strftime('%m/%d/%Y')

    iron_obj = iron_data(chart_type = "1week" , data = data, date = date)
    iron_obj.save()
    iron_obj = iron_data(chart_type = "1month" , data = data, date = date)
    iron_obj.save()
    iron_obj = iron_data(chart_type = "3month" , data = data, date = date)
    iron_obj.save()
    iron_obj = iron_data(chart_type = "6month" , data = data, date = date)
    iron_obj.save()
    iron_obj = iron_data(chart_type = "1year" , data = data, date = date)
    iron_obj.save()
    iron_obj = iron_data(chart_type = "2year" , data = data, date = date)
    iron_obj.save()

    iron_obj = iron_data.objects.filter(chart_type = "1week").first()
    iron_obj.delete()
    iron_obj = iron_data.objects.filter(chart_type = "1month").first()
    iron_obj.delete()
    iron_obj = iron_data.objects.filter(chart_type = "3month").first()
    iron_obj.delete()
    iron_obj = iron_data.objects.filter(chart_type = "6month").first()
    iron_obj.delete()
    iron_obj = iron_data.objects.filter(chart_type = "1year").first()
    iron_obj.delete()
    iron_obj = iron_data.objects.filter(chart_type = "2year").first()
    iron_obj.delete()
    return()