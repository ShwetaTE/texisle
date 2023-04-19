from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from newspaper.extractors import RE_LANG
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
from django_pandas.io import read_frame
import requests
import json
from django.utils import timezone
import after_response

# sends back the latest app versiona and changelog
@api_view(['POST'])
def version_check(request):
    app = request.data["app"]
    deviceID = request.data['deviceID']
    app_vr = request.data['app_vr']
    os = request.data['os']
    data_obj = version_info.objects.filter(app = app, os = os)
    # print(data_obj)
    for each in data_obj:
        vr = each.version
        red_url = each.url
    changelog_obj = changelogs.objects.filter(version = vr, app = app, os = os)
    for each in changelog_obj:
        change = each.changelog

    # if app_vr != vr:
    #     print("version not up to date")
    #     change_terms.after_response(deviceID, app_vr, app)
    # else:
    #     print("version up to date")

    return Response({"version": vr, "url": red_url, "changelog": change})

@after_response.enable
def change_terms(deviceID, app_vr, app):
    dt = datetime.now(tz=timezone.utc)
    try:
        a = customer_table.objects.get(deviceID = deviceID, app = app)
        a.Terms = "N"
        a.save()
        print("customer present")
    except:
        data_obj = customer_table(deviceID = deviceID, app = app, created_time = dt, Terms = "N")
        data_obj.save()


############################################################################################

# depricated
@api_view(['GET'])
def version(request):
    url = "https://appho.st/api/get_current_version/?u=ZkffMofyBYXhMnGXI9Drh3c8ujo1&a=4sB0kQffEoMktIgdTqa2&platform=ios"
    response = requests.request("GET", url, headers={}, data={})
    res = json.loads(response.text)
    # print(res)
    vr = res["version"]
    res_url = res["url"]
    data_obj = changelogs.objects.filter(version = vr)
    for each in data_obj:
        change = each.changelog
    return Response({"version": vr, "url": res_url, "changelog": change})

@api_view(['POST'])
def version_check_old(request):
    app = request.data["app"]
    if app == "test":
        url = "https://appho.st/api/get_current_version/?u=ZkffMofyBYXhMnGXI9Drh3c8ujo1&a=E9djWV5wLAQWuHc7P2AI&platform=ios"
    if app == "prod":
        url = "https://appho.st/api/get_current_version/?u=ZkffMofyBYXhMnGXI9Drh3c8ujo1&a=4sB0kQffEoMktIgdTqa2&platform=ios"
    response = requests.request("GET", url, headers={}, data={})
    res = json.loads(response.text)
    # print(res)
    vr = res["version"]
    res_url = res["url"]
    data_obj = changelogs.objects.filter(version = vr, app = app)
    for each in data_obj:
        change = each.changelog
    return Response({"version": vr, "url": res_url, "changelog": change})

