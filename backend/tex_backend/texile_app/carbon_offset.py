from unittest import result
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

# the calculation for carbon offsset is done over here

@api_view(['POST'])
def carbon_offset_calc(request):
    product = request.data["product"]
    if product == "OCTG":
        quantity = float(request.data["quantity"])
        weight = float(request.data["weight"])
        data_obj = carbon_factor.objects.values('factor').filter(product = product)[0]
        co2_factor = float(data_obj['factor'])
        print(co2_factor)
        result = ((quantity*weight)/2000)*co2_factor
        result = round(result,3)
    if product == "LinePipe":
        quantity = float(request.data["quantity"])
        weight = float(request.data["weight"])
        ppf = float(request.data["ppf"])
        data_obj = carbon_factor.objects.values('factor').filter(product = product)[0]
        co2_factor = float(data_obj['factor'])
        result = ((quantity*(10.69*(weight - ppf)*ppf))/2000)*co2_factor
        result = round(result,3)
    return Response({"status":200,"result": result})