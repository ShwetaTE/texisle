from tabnanny import check
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from newspaper.extractors import RE_LANG
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
from django_pandas.io import read_frame
from numpy import ERR_CALL
import pandas as pd
import pandas_market_calendars as mcal
import numpy as np
import time, os
from datetime import datetime
from datetime import datetime, timedelta, date
from django.utils import timezone
import io
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from django.db.models import Q
# api to download data on website
@api_view(['POST'])
def web_data(request):
    chart_list = request.data["chart_list"]
    print(chart_list)
    start_date = request.data["start"]
    end_date = request.data["end"]
    email = request.data['email']
    try:
        upd_config = request.data['upd_config']
    except:
        upd_config = 1
    if upd_config == 1:
        save_config(chart_list, email)
    result_df = fill_date_column(start_date, end_date)
    # print(result_df)
    for each in chart_list:
        # print(each)
        data_df = check_table(each)
        # print(data_df)
        result_df = result_df.join(data_df.set_index('date'), on='date')
    #     print(result_df)
    # print(result_df)
    result_df = result_df.fillna('')
    data = result_df.values.tolist()
    return Response(data)

# api to send data via email
@api_view(['POST'])
def web_data_df(request):
    chart_list = request.data["chart_list"]
    start_date = request.data["start"]
    end_date = request.data["end"]
    email = request.data['email']
    try:
        upd_config = request.data['upd_config']
    except:
        upd_config = 1
    if upd_config == 1:
        save_config(chart_list, email)
    result_df = fill_date_column(start_date, end_date)
    # print(result_df)
    for each in chart_list:
        # print(each)
        data_df = check_table(each)
        # print(data_df)
        result_df = result_df.join(data_df.set_index('date'), on='date')
        # print(result_df)
    # print(result_df)
    result_df = result_df.fillna('')
    # data = result_df.values.tolist()
    send_csv_mail(result_df, email, chart_list, start_date, end_date)
    return Response({"status":200})

def check_table(ticker):
    # f = ['HO=F','RB=F','F_index']
    rmi = ['SCRAP','HRC','COAL','IRONORE','RMI_index']
    iom = ['RIO','VALE','SXC','BHP','IOM_index']
    pmf = ['TS','VKPA','TMST','X','NWPX','PMF_index']
    smf = ['STLD','RS','CLF','TX','GGB','CMC','MT','PKX','NUE','TKADE','SZGDE','NIPPON','JFE','SMF_index']
    transportation = ['ULSD','Baltic','Truck','CassFreight','All-Grade','T_index']
    rc = ['Ardmore', 'Arkoma', 'Barnett', 'Cana', 'Niobrara', 'Ford', 'Granite', 'Haynesville', 'Marcellus', 'Mississippian', 'Permian', 'Utica', 'Williston','RC_index']
    wc = ['Anadarko_DUC', 'Appalachia_DUC', 'Bakken_DUC', 'Eagle_DUC', 'Haynesville_DUC', 'Niobrara_DUC', 'Permian_DUC', 'DPR_DUC']
    # if ticker in f:
    #     data = f_data_df(ticker)
    if ticker in rmi:
        data = rmi_data_df(ticker)
    if ticker in iom:
        data = iom_data_df(ticker)
    if ticker in pmf:
        data = pmf_data_df(ticker)
    if ticker in smf:
        data = smf_data_df(ticker)
    if ticker in transportation:
        data = t_data_df(ticker)
    if ticker in rc:
        data = rc_data_df(ticker)
    if ticker in wc:
        data = wc_data_df(ticker)
    return(data)

def rmi_data_df(ticker):
    data_obj = index_rmi_cme_data.objects.all()
    data_df = read_frame(data_obj, fieldnames=['date',ticker])
    return(data_df)

def iom_data_df(ticker):
    data_obj = index_iom_data.objects.all()
    data_df = read_frame(data_obj, fieldnames=['date',ticker])
    return(data_df)

def smf_data_df(ticker):
    data_obj = index_smf_data.objects.all()
    data_df = read_frame(data_obj, fieldnames=['date',ticker])
    return(data_df)

def pmf_data_df(ticker):
    data_obj = index_pmf_data.objects.all()
    data_df = read_frame(data_obj, fieldnames=['date',ticker])
    return(data_df)

def t_data_df(ticker):
    data_obj = transportation_data.objects.filter(chart = ticker)
    lst = []
    for n in data_obj:
        temp= [n.date, n.data]
        lst.append(temp)
    for i in lst:
        i[0] = i[0].replace("-","/")
    data_df = pd.DataFrame(lst, columns =['date',ticker])
    return(data_df)

def rc_data_df(ticker):
    data_obj = index_rig_data.objects.all()
    data_df = read_frame(data_obj, fieldnames=['date',ticker])
    print(data_df.columns)
    data_df.rename(columns ={ticker : ticker + " Rig_Count"}, inplace=True)
    print(data_df.columns)
    return(data_df)

def wc_data_df(ticker):
    data_obj = index_duc_data.objects.all()
    ticker = ticker[:-4]
    print(ticker)
    data_df = read_frame(data_obj, fieldnames=['date',ticker+"_D",ticker+"_C",ticker+"_DUC"])
    return(data_df)

# def f_data_df(ticker):
#     data_obj = index_f_data.objects.all()
#     data_df = read_frame(data_obj, fieldnames=['date',ticker])
#     return(data_df)

def fill_date_column(start_date, end_date):
    presentday = datetime.now()
    date = presentday - timedelta(days = 1)
    dt = date.strftime('%Y-%m-%d')
    # Create a calendar
    nyse = mcal.get_calendar('NYSE')
    # early = nyse.schedule(start_date='2020-01-01', end_date=dt)
    early = nyse.schedule(start_date = start_date, end_date = end_date)
    date_list = []
    list = mcal.date_range(early, frequency='1D')
    for each in list:
        dt = each.strftime('%m/%d/%Y')
        date_list.append(dt)
    date_df = pd.DataFrame(date_list, columns =['date'])
    return(date_df)

def save_config(chart_list, email):
    list1 = chart_list
    str1 = ' '.join(list1)
    try:
        print("here ", str1)
        a = website_viewers.objects.get(email_id = email)
        a.config = str1
        a.save()
    except:
        dt = datetime.now(tz=timezone.utc)
        data_obj = website_viewers(email_id = email, created_time = dt, config = str1)
        data_obj.save()

@api_view(['POST'])
def get_config(request):
    email = request.data['email']
    try:
        a = website_viewers.objects.all().filter(email_id = email)[0]
        str = a.config
        chart_list = list(str.split(" "))
        return Response({"chart_list":chart_list, "exist":1})
    except:
        dt = datetime.now(tz=timezone.utc)
        data_obj = website_viewers(email_id = email, created_time = dt)
        data_obj.save()
        return Response({"chart_list":[], "exist":0})

@api_view(['POST'])
def get_emailID(request):
    deviceID = request.data['deviceID']
    app = request.data['app']
    try:
        a = customer_table.objects.all().filter(deviceID = deviceID, app = app)[0]
        emailID = a.emailID
        print(emailID)
        if emailID == '':
            return Response({"exist":0})
        else:
            return Response({"emailID":emailID, "exist":1})
    except:
        return Response({"exist":0})

@api_view(['POST'])
def add_emailID(request):
    deviceID = request.data['deviceID']
    app = request.data['app']
    emailID = request.data['emailID']
    data_obj = customer_table.objects.all().filter(deviceID = deviceID, app = app)[0]
    data_obj.emailID = emailID
    data_obj.save()
    return Response({'status':200})


def send_csv_mail(df, email, chart_list, start_date, end_date):
    custom_message=customMessage.objects.all().filter(Q(title__iexact='references')|Q(title__iexact='frequency of update'))
    mail_body=""
    print(custom_message)
    for each in custom_message:
        if(each.title!='about'):
            mail_body=mail_body+'<p><h3 style="color:red">'+each.title.capitalize()+ '</h3></p>'+'<h5>'+each.message+ '</h5>'
    print(chart_list)
    chart = ""
    for each in chart_list:
        chart = chart + each + " "
    print(chart)
    mail_content = "Tickers: "+chart +"\nDate range: "+start_date+" to "+end_date +mail_body
    sender_address = 'businessinsights@texisle.com'
    sender_pass = 'xymfnfqkrxzwqfkl' #'PipeIntel2022$'
    receiver_address = [email]
    EXPORTERS = {'PipeIntel_data.csv': export_csv}

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = ", ".join(receiver_address)
    message['Subject'] = 'Pipe Intel Data'   #The subject line

    for filename in EXPORTERS:   
        attachment = MIMEApplication(EXPORTERS[filename](df))
        attachment['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        message.attach(attachment)
    message.attach(MIMEText(mail_content, 'html'))

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.outlook.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

def export_csv(df):
  with io.StringIO() as buffer:
    df.to_csv(buffer)
    return buffer.getvalue()