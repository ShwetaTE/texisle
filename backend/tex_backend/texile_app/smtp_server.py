from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from newspaper.extractors import RE_LANG
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
from django_pandas.io import read_frame
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter.messagebox import RETRY
from django.utils import timezone
import after_response

@api_view(['POST'])
def send_mail(request):
    content = request.data["content"]
    mail_content = content
    email_obj = emails.objects.all().filter(archive = 'N')
    receiver_address = []
    for each in email_obj:
        receiver_address.append(each.email)
    #The mail addresses and password
    print(receiver_address)
    sender_address = 'pipeintelte@gmail.com'
    sender_pass = 'owsqeqnvrwxlylet' #'czzganlwgitwnqgq' #th1rd3y3
    # receiver_address = ['atri@thirdeyedata.io']
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    # message['To'] = receiver_address
    message['To'] = ", ".join(receiver_address)
    message['Subject'] = 'Error Monitoring notification system'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) # 465) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

    return Response({"status":200})

# @api_view(['POST'])
@after_response.enable
def feedback_mail(request):
    name = request.data["name"]
    phone = request.data["phone"]
    comment = request.data["comment"]
    email = request.data['email']
    rating = request.data["rating"]
    mail_content = "Name: "+ name +"\nPhone Number: "+ phone +"\nEmail: "+ email +"\nRating: "+ rating + "\nComments: "+ comment
    email_obj = emails.objects.all().filter(archive = 'N')
    receiver_address = []
    for each in email_obj:
        receiver_address.append(each.email)
    #The mail addresses and password
    print(receiver_address)
    sender_address = 'businessinsights@texisle.com'
    sender_pass = 'xymfnfqkrxzwqfkl'
    # receiver_address = ['atri@thirdeyedata.io']
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    # message['To'] = receiver_address
    message['To'] = ", ".join(receiver_address)
    message['Subject'] = 'Pipe Intel Feedback'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.outlook.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

# Depricated
@api_view(['POST'])
def send_download_link(request):
    dt = datetime.now(tz=timezone.utc)
    receiver_address = []
    address = request.data["receiver_address"]
    try:
        a = website_viewers.objects.get(email_id = address)
        print("email present")
    except:
        data_obj = website_viewers(email_id = address, created_time = dt)
        data_obj.save()
    receiver_address.append(address)
    mail_content = "Website Link: https://www.texisle-pipeintel.com/"
    #The mail addresses and password
    print(receiver_address)
    sender_address = 'businessinsights@texisle.com'
    sender_pass = 'xymfnfqkrxzwqfkl' #'PipeIntel2022$'
    # receiver_address = ['atri@thirdeyedata.io']
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    # message['To'] = receiver_address
    message['To'] = ", ".join(receiver_address)
    message['Subject'] = 'Pipe Intel Data Website'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.outlook.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

    return Response({"status":200})
