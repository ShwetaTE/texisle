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

@api_view(['GET'])
def y_stock_data(request):
    chart_name = ['scrap','hrc','MFFH22.NYM','iron','raw_material_index','RIO','VALE','SXC','BHP','iron_ore','TS','VK.PA','X','TMST','NWPX','pipe_manufacturing','MT','PKX','NUE','STLD','RS','CLF','TX','GGB','CMC','TKA.DE','SZG.DE','5401.T','5411.T','steel_manufacturing','Baltic','ULSD','All-Grade','CassFreight','Truck','transport', 'Ardmore', 'Arkoma', 'Barnett', 'Cana', 'Niobrara', 'Ford', 'Granite', 'Haynesville', 'Marcellus', 'Mississippian', 'Permian', 'Utica', 'Williston', 'rc_index', 'Anadarko_DUC', 'Appalachia_DUC', 'Bakken_DUC', 'Eagle_DUC', 'Haynesville_DUC', 'Niobrara_DUC', 'Permian_DUC', 'DPR_DUC']
    ticker_name = ['scrap_data', 'hrc_data', 'coal_data', 'iron_data', 'raw_material_index', 'rio_data', 'vale_data', 'sxc_data', 'bhp_data', 'iron_ore', 'ts_data', 'vkpa_data', 'x_data', 'tmst_data', 'nwpx_data', 'pipe_manufacturing', 'mt_data', 'pkx_data', 'nue_data', 'stld_data', 'rs_data', 'clf_data', 'tx_data', 'ggb_data', 'cmc_data', 'tkade_data', 'szgde_data', 'nippon_data', 'jfe_data', 'steel_manufacturing', 'baltic_data', 'usld_data', 'ag_data', 'cf_data', 'truck_data', 't_index', 'Ardmore_data', 'Arkoma_data', 'Barnett_data', 'Cana_data', 'Niobrara_data', 'Ford_data', 'Granite_data', 'Haynesville_data', 'Marcellus_data', 'Mississippian_data', 'Permian_data', 'Utica_data', 'Williston_data', 'rc_index', 'Anadarko_DUC', 'Appalachia_DUC', 'Bakken_DUC', 'Eagle_DUC', 'Haynesville_DUC', 'Niobrara_DUC', 'Permian_DUC', 'DPR_DUC']
    data = {}
    print(len(chart_name))
    print(len(ticker_name))
    data_obj = stock_data.objects.all()
    for each in data_obj:
        try:
            chart = (each.chart_type)
            index = chart_name.index(chart)
            c_name = ticker_name[index]
            print(chart)
            print(c_name)
            temp_data = {
                "data": each.data,
                "current": each.current
            }
            temp = {c_name: temp_data}
            data.update(temp)
        except:
            # temp_data = {
            #     "data": 0,
            #     "current": 0
            # }
            # temp = {c_name: temp_data}
            # data.update(temp)
            print(each.chart_type + " not in list")
    return Response({"stock_data":data})

# not in use anymore(DEPRICATED)
@csrf_exempt
@api_view(['GET'])
def stock_data_new(request):
    # sm_obj = stock_data.objects.all().filter(chart_type = "steel_market")
    # sm_data = {"data": 0, "current": 0}
    # for n in sm_obj:
    #     sm_data = {
    #         "data": n.data,
    #         "current": n.current
    #     }
    pm_obj = stock_data.objects.all().filter(chart_type = "pipe_manufacturing")
    pm_data = {"data": 0, "current": 0}
    for n in pm_obj:
        pm_data = {
            "data": n.data,
            "current": n.current
        }
    smf_obj = stock_data.objects.all().filter(chart_type = "steel_manufacturing")
    smf_data = {"data": 0, "current": 0}
    for n in smf_obj:
        smf_data = {
            "data": n.data,
            "current": n.current
        }
    io_obj = stock_data.objects.all().filter(chart_type = "iron_ore")
    io_data = {"data": 0, "current": 0}
    for n in io_obj:
        io_data = {
            "data": n.data,
            "current": n.current
        }
    # f_obj = stock_data.objects.all().filter(chart_type = "fuel")
    # f_data = {"data": 0, "current": 0}
    # for n in f_obj:
    #     f_data = {
    #         "data": n.data,
    #         "current": n.current
    #     }
    rmi_obj = stock_data.objects.all().filter(chart_type = "raw_material_index")
    rmi_data = {"data": 0, "current": 0}
    for n in rmi_obj:
        rmi_data = {
            "data": n.data,
            "current": n.current
        }
    scrap_obj = stock_data.objects.all().filter(chart_type = "scrap")
    scrap_data = {"data": 0, "current": 0}
    for n in scrap_obj:
        scrap_data = {
            "data": n.data,
            "current": n.current
        }
    # print(scrap_data)
    hrc_obj = stock_data.objects.all().filter(chart_type = "hrc")
    hrc_data = {"data": 0, "current": 0}
    for n in hrc_obj:
        hrc_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)
    iron_obj = stock_data.objects.all().filter(chart_type = "iron")
    iron_data = {"data": 0, "current": 0}
    for n in iron_obj:
        iron_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)
    rio_obj = stock_data.objects.all().filter(chart_type = "RIO")
    rio_data = {"data": 0, "current": 0}
    for n in rio_obj:
        rio_data = {
            "data": n.data,
            "current": n.current
        }
    # print(scrap_data)
    vale_obj = stock_data.objects.all().filter(chart_type = "VALE")
    vale_data = {"data": 0, "current": 0}
    for n in vale_obj:
        vale_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)
    mt_obj = stock_data.objects.all().filter(chart_type = "MT")
    mt_data = {"data": 0, "current": 0}
    for n in mt_obj:
        mt_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)
    pkx_obj = stock_data.objects.all().filter(chart_type = "PKX")
    pkx_data = {"data": 0, "current": 0}
    for n in pkx_obj:
        pkx_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)
    nue_obj = stock_data.objects.all().filter(chart_type = "NUE")
    nue_data = {"data": 0, "current": 0}
    for n in nue_obj:
        nue_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)
    ts_obj = stock_data.objects.all().filter(chart_type = "TS")
    ts_data = {"data": 0, "current": 0}
    for n in ts_obj:
        ts_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)
    vlouf_obj = stock_data.objects.all().filter(chart_type = "VLOUF")
    vlouf_data = {"data": 0, "current": 0}
    for n in vlouf_obj:
        vlouf_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)
    stld_obj = stock_data.objects.all().filter(chart_type = "STLD")
    stld_data = {"data": 0, "current": 0}
    for n in stld_obj:
        stld_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)
    rs_obj = stock_data.objects.all().filter(chart_type = "RS")
    rs_data = {"data": 0, "current": 0}
    for n in rs_obj:
        rs_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)
    clf_obj = stock_data.objects.all().filter(chart_type = "CLF")
    clf_data = {"data": 0, "current": 0}
    for n in clf_obj:
        clf_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)
    tx_obj = stock_data.objects.all().filter(chart_type = "TX")
    tx_data = {"data": 0, "current": 0}
    for n in tx_obj:
        tx_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)
    ggb_obj = stock_data.objects.all().filter(chart_type = "GGB")
    ggb_data = {"data": 0, "current": 0}
    for n in ggb_obj:
        ggb_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)
    x_obj = stock_data.objects.all().filter(chart_type = "X")
    x_data = {"data": 0, "current": 0}
    for n in x_obj:
        x_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)
    cmc_obj = stock_data.objects.all().filter(chart_type = "CMC")
    cmc_data = {"data": 0, "current": 0}
    for n in cmc_obj:
        cmc_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)
    sxc_obj = stock_data.objects.all().filter(chart_type = "SXC")
    sxc_data = {"data": 0, "current": 0}
    for n in sxc_obj:
        sxc_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)
    tmst_obj = stock_data.objects.all().filter(chart_type = "TMST")
    tmst_data = {"data": 0, "current": 0}
    for n in tmst_obj:
        tmst_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)
    bhp_obj = stock_data.objects.all().filter(chart_type = "BHP")
    bhp_data = {"data": 0, "current": 0}
    for n in bhp_obj:
        bhp_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)

    # hof_obj = stock_data.objects.all().filter(chart_type = "HO=F")
    # hof_data = {"data": 0, "current": 0}
    # for n in hof_obj:
    #     hof_data = {
    #         "data": n.data,
    #         "current": n.current
    #     }
    # # print(hrc_data)

    # rbf_obj = stock_data.objects.all().filter(chart_type = "RB=F")
    # rbf_data = {"data": 0, "current": 0}
    # for n in rbf_obj:
    #     rbf_data = {
    #         "data": n.data,
    #         "current": n.current
    #     }
    # print(hrc_data)

    coal_obj = stock_data.objects.all().filter(chart_type = "MFFH22.NYM")
    coal_data = {"data": 0, "current": 0}
    for n in coal_obj:
        coal_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)

    nwpx_obj = stock_data.objects.all().filter(chart_type = "NWPX")
    nwpx_data = {"data": 0, "current": 0}
    for n in nwpx_obj:
        nwpx_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)

    vkpa_obj = stock_data.objects.all().filter(chart_type = "VK.PA")
    vkpa_data = {"data": 0, "current": 0}
    for n in vkpa_obj:
        vkpa_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)

    tkade_obj = stock_data.objects.all().filter(chart_type = "TKA.DE")
    tkade_data = {"data": 0, "current": 0}
    for n in tkade_obj:
        tkade_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)

    szgde_obj = stock_data.objects.all().filter(chart_type = "SZG.DE")
    szgde_data = {"data": 0, "current": 0}
    for n in szgde_obj:
        szgde_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)

    nippon_obj = stock_data.objects.all().filter(chart_type = "5401.T")
    nippon_data = {"data": 0, "current": 0}
    for n in nippon_obj:
        nippon_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)

    jfe_obj = stock_data.objects.all().filter(chart_type = "5411.T")
    jfe_data = {"data": 0, "current": 0}
    for n in jfe_obj:
        jfe_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)

    usld_obj = stock_data.objects.all().filter(chart_type = "ULSD")
    usld_data = {"data": 0, "current": 0}
    for n in usld_obj:
        usld_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)

    baltic_obj = stock_data.objects.all().filter(chart_type = "Baltic")
    baltic_data = {"data": 0, "current": 0}
    for n in baltic_obj:
        baltic_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)

    truck_obj = stock_data.objects.all().filter(chart_type = "Truck")
    truck_data = {"data": 0, "current": 0}
    for n in truck_obj:
        truck_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)

    cf_obj = stock_data.objects.all().filter(chart_type = "CassFreight")
    cf_data = {"data": 0, "current": 0}
    for n in cf_obj:
        cf_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)

    ag_obj = stock_data.objects.all().filter(chart_type = "All-Grade")
    ag_data = {"data": 0, "current": 0}
    for n in ag_obj:
        ag_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)

    t_obj = stock_data.objects.all().filter(chart_type = "transport")
    t_data = {"data": 0, "current": 0}
    for n in t_obj:
        t_data = {
            "data": n.data,
            "current": n.current
        }
    # print(hrc_data)

    data={
        # "steel_market":sm_data,
        "pipe_manufacturing":pm_data,
        "steel_manufacturing":smf_data,
        "iron_ore":io_data,
        # "fuel":f_data,
        "raw_material_index":rmi_data,
        "t_index":t_data,
        "rio_data":rio_data,
        "vale_data":vale_data,
        "mt_data":mt_data,
        "pkx_data":pkx_data,
        "nue_data":nue_data,
        "ts_data":ts_data,
        "vlouf_data":vlouf_data,
        "stld_data":stld_data,
        "rs_data":rs_data,
        "clf_data":clf_data,
        "tx_data":tx_data,
        "ggb_data":ggb_data,
        "x_data":x_data,
        "cmc_data":cmc_data,
        "sxc_data":sxc_data,
        "tmst_data":tmst_data,
        "bhp_data":bhp_data,
        # "hof_data":hof_data,
        # "rbf_data":rbf_data,
        "coal_data":coal_data,
        "nwpx_data":nwpx_data,
        "vkpa_data":vkpa_data,
        "tkade_data":tkade_data,
        "szgde_data":szgde_data,
        "nippon_data":nippon_data,
        "jfe_data":jfe_data,
        "usld_data":usld_data,
        "truck_data": truck_data,
        "baltic_data":baltic_data,
        "cf_data":cf_data,
        "scrap_data":scrap_data,
        "hrc_data":hrc_data,
        "iron_data":iron_data,
        "ag_data": ag_data,
    }
    return Response({"stock_data":data})
