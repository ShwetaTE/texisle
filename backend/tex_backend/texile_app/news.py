from django.shortcuts import render
from django.http import HttpResponse, HttpRequest , JsonResponse
from .models import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, schema, permission_classes
import json
from django.core import serializers
import time as tm
import os
from datetime import datetime
import datetime
from newspaper import Article
from newspaper import Config
from urllib.parse import urljoin, urlparse

#api for all tabs(tickers)
@csrf_exempt
@api_view(['POST'])
def news_data_updated(request):
    chart_type= request.data["chart_type"]
    news_obj = News_data.objects.all().filter(tab_name = chart_type, archive = 'N')
    # news_obj = News_data_test.objects.all().filter(tab_name = chart_type, archive = 'N')
    data = []
    relevant_data = []
    non_relevant_data = []
    for n in news_obj:
        b = n.date.replace(tzinfo=None)
        print(b)
        a = datetime.datetime.now().replace(microsecond=0)
        # get timedifference for news artticles
        date = a-b
        converted_date=str(date).split(',')
        if len(converted_date)>1:
            if int(converted_date[0].split(' ')[0])<1:
                time=converted_date[1].split(':')[0]+" Hr"
            else:
                time=converted_date[0]
        else:
            if int(converted_date[0].split(':')[0])==0:
                if converted_date[0].split(':')[1]=='00':
                    temp=int(converted_date[0].split(':')[2])
                    time=str(temp) +" sec"
                else:
                    temp=int(converted_date[0].split(':')[1])
                    time=str(temp) + " min"
            else:
                temp=int(converted_date[0].split(':')[0])
                time=str(temp)+" Hr"
        image = n.image
        if image == "":
            try:
                first_article = Article(url=n.link, language='en')
                first_article.download()
                first_article.parse()
                image = first_article.top_image
            except:
                # print("2")
                image = "https://upload.wikimedia.org/wikipedia/commons/d/d1/Image_not_available.png"
                print("no image found")
            a = News_data.objects.get(link=n.link, tab_name = chart_type, relevance_level_tab=n.relevance_level_tab)
            # a = News_data_test.objects.get(link=n.link, tab_name = chart_type, relevance_level_tab=n.relevance_level_tab)
            a.image = image
            a.save()

        list = {
            "title":n.title,
            "link":n.link,
            "website":n.website,
            "image":image,
            "date":time,
            "relevance": n.relevance_level_tab
        }
        if list['relevance'] == 99:
            non_relevant_data.append(list)
        else:
            relevant_data.append(list)
    data = sorted(relevant_data, key=lambda k: k['relevance'], reverse=False) 
    non_relevant_data.reverse()
    for each in non_relevant_data:
        data.append(each)
    return Response({"data": data})

#api for index page(landing page)
@csrf_exempt
@api_view(['GET'])
def default_news_data(request):
    news_obj = News_data.objects.all().filter(on_landing_page = "Y", archive = 'N')
    # print(news_obj.values())
    
    # news_obj = News_data_test.objects.all().filter(on_landing_page = "Y", archive = 'N')
    data = []
    relevant_data = []
    non_relevant_data = []
    for n in news_obj:
        b = n.date.replace(tzinfo=None)
        a = datetime.datetime.now().replace(microsecond=0)
        date = a-b
        converted_date=str(date).split(',')
        if len(converted_date)>1:
            if int(converted_date[0].split(' ')[0])<1:
                time=converted_date[1].split(':')[0]+" Hr"
            else:
                time=converted_date[0]
        else:
            if int(converted_date[0].split(':')[0])==0:
                if converted_date[0].split(':')[1]=='00':
                    temp=int(converted_date[0].split(':')[2])
                    time=str(temp) +" sec"
                else:
                    temp=int(converted_date[0].split(':')[1])
                    time=str(temp) + " min"
            else:
                temp=int(converted_date[0].split(':')[0])
                time=str(temp)+" Hr"
        image = n.image
        if image == "":
            try:
                first_article = Article(url=n.link, language='en')
                first_article.download()
                first_article.parse()
                image = first_article.top_image
            except:
                image="https://upload.wikimedia.org/wikipedia/commons/d/d1/Image_not_available.png"
                print("no image found")
            a = News_data.objects.get(link=n.link, on_landing_page = "Y")
            # a = News_data_test.objects.get(link=n.link, on_landing_page = "Y")
            a.image= image
            a.save()

        list = {
            "title":n.title,
            "link":n.link,
            "website":n.website,
            "image":image,
            "date":time,
            "relevance": n.relevance_level_landing_page
        }
        data.append(list)
        if list['relevance'] == 99:
            non_relevant_data.append(list)
        else:
            relevant_data.append(list)
    data = sorted(relevant_data, key=lambda k: k['relevance'], reverse=False)
    print(data)
    non_relevant_data.reverse()
    for each in non_relevant_data:
        data.append(each)
    return Response({"data": data})

#api for all parent tabs(index)
@csrf_exempt
@api_view(['POST'])
def news_data_index(request):
    # print(request.data)
    chart_type= request.data["chart_type"]
    news_obj = News.objects.all().filter(chart = chart_type, archive = 'N')
    # news_obj = News_test.objects.all().filter(chart = chart_type, archive = 'N')
    data = []
    relevant_data = []
    non_relevant_data = []
    for n in news_obj:
        # print(n.link)
        # list = [n.title, n.link, n.website]
        b = n.date.replace(tzinfo=None)
        a = datetime.datetime.now().replace(microsecond=0)
        # print("a--> ",a)
        # print("b--> ",b)
        date = a-b
        converted_date=str(date).split(',')
        # print(converted_date)
        if len(converted_date)>1:
            if int(converted_date[0].split(' ')[0])<1:
                time=converted_date[1].split(':')[0]+" Hr"
            else:
                time=converted_date[0]
        else:
            if int(converted_date[0].split(':')[0])==0:
                if converted_date[0].split(':')[1]=='00':
                    temp=int(converted_date[0].split(':')[2])
                    time=str(temp) +" sec"
                else:
                    temp=int(converted_date[0].split(':')[1])
                    time=str(temp) + " min"
            else:
                temp=int(converted_date[0].split(':')[0])
                time=str(temp)+" Hr"
        image = n.image
        if image == "":
            try:
                first_article = Article(url=n.link, language='en')
                first_article.download()
                first_article.parse()
                image = first_article.top_image
            except:
                # print("2")
                image = "https://upload.wikimedia.org/wikipedia/commons/d/d1/Image_not_available.png"
                print("no image found")
            a = News.objects.get(link=n.link, chart = chart_type)
            # a = News_test.objects.get(link=n.link, chart = chart_type)
            a.image = image
            a.save()

        list = {
            "title":n.title,
            "link":n.link,
            "website":n.website,
            "image":image,
            "date":time,
            "relevance": n.relevance_level
        }
        if list['relevance'] == 99:
            non_relevant_data.append(list)
        else:
            relevant_data.append(list)
    data = sorted(relevant_data, key=lambda k: k['relevance'], reverse=False) 
    non_relevant_data.reverse()
    for each in non_relevant_data:
        data.append(each)
    # print(data)
    return Response({"data": data})

# update the image links
@api_view(['GET'])
def news_image_fetch(request):
    news_obj = News_data.objects.all().filter(archive = 'N')
    # news_obj = News_data_test.objects.all().filter(archive = 'N')
    for n in news_obj:
        image = n.image
        if image == "":
            try:
                first_article = Article(url=n.link, language='en')
                first_article.download()
                first_article.parse()
                image = first_article.top_image
            except:
                # print("2")
                image = "https://upload.wikimedia.org/wikipedia/commons/d/d1/Image_not_available.png"
                print("no image found")
            a = News_data.objects.get(link=n.link, tab_name = n.tab_name,  relevance_level_landing_page = n.relevance_level_landing_page, relevance_level_tab = n.relevance_level_tab)
            # a = News_data_test.objects.get(link=n.link, tab_name = n.tab_name,  relevance_level_landing_page = n.relevance_level_landing_page, relevance_level_tab = n.relevance_level_tab)
            a.image = image
            a.save()
    
    news_obj = News.objects.all().filter(archive = 'N')
    # news_obj = News_test.objects.all().filter(archive = 'N')
    for n in news_obj:
        image = n.image
        if image == "":
            try:
                first_article = Article(url=n.link, language='en')
                first_article.download()
                first_article.parse()
                image = first_article.top_image
            except:
                image = "https://upload.wikimedia.org/wikipedia/commons/d/d1/Image_not_available.png"
                print("no image found")
            a = News.objects.get(link=n.link, chart = n.chart, relevance_level = n.relevance_level)
            # a = News_test.objects.get(link=n.link, chart = n.chart, relevance_level = n.relevance_level)
            a.image = image
            a.save()

    return Response({"data": 200})

# remove parameters from the news url, mainly for Zacks articles
@api_view(['GET'])
def news_remove_parameter(request):
    news_obj = News_data.objects.all().filter(archive = 'N', website = 'Zacks')
    for n in news_obj:
        url = n.link
        link = urljoin(url, urlparse(url).path)
        print(link)  
        n.link = link
        n.save()
    
    news_obj = News.objects.all().filter(archive = 'N', website = 'Zacks')
    for n in news_obj:
        url = n.link
        link = urljoin(url, urlparse(url).path)
        print(link)  
        n.link = link
        n.save()
    
    return Response({"status": 200})

##########################################################################
# reccomended news
@api_view(['GET'])
def rec_news_lp(request):
    news_obj = News_rec.objects.all().filter(on_landing_page = "Y", archive = 'N')
    data = []
    relevant_data = []
    non_relevant_data = []
    for n in news_obj:
        b = n.date.replace(tzinfo=None)
        a = datetime.datetime.now().replace(microsecond=0)
        date = a-b
        converted_date=str(date).split(',')
        if len(converted_date)>1:
            if int(converted_date[0].split(' ')[0])<1:
                time=converted_date[1].split(':')[0]+" Hr"
            else:
                time=converted_date[0]
        else:
            if int(converted_date[0].split(':')[0])==0:
                if converted_date[0].split(':')[1]=='00':
                    temp=int(converted_date[0].split(':')[2])
                    time=str(temp) +" sec"
                else:
                    temp=int(converted_date[0].split(':')[1])
                    time=str(temp) + " min"
            else:
                temp=int(converted_date[0].split(':')[0])
                time=str(temp)+" Hr"
        image = n.image
        title = n.title
        id = n.id
        if image == "":
            try:
                first_article = Article(url=n.link, language='en')
                first_article.download()
                first_article.parse()
                image = first_article.top_image
            except:
                image = "https://upload.wikimedia.org/wikipedia/commons/d/d1/Image_not_available.png"
                print("no image found")
            a = News_rec.objects.get(id = id)
            a.image = image
            a.save()
        if title == "":
            try:
                first_article = Article(url=n.link, language='en')
                first_article.download()
                first_article.parse()
                title = first_article.title
            except:
                try:
                    first_article = Article(url=n.link, language='en')
                    first_article.download()
                    first_article.parse()
                    title = first_article.summary
                except:
                    first_article = Article(url=n.link, language='en')
                    first_article.download()
                    first_article.parse()
                    title = first_article.text[:50] + "...."
            a = News_rec.objects.get(id = id)
            a.title = title
            a.save()

        list = {
            "title":n.title,
            "link":n.link,
            "website":n.website,
            "image":image,
            "date":time,
            "relevance": n.relevance_level_landing_page
        }
        data.append(list)
        if list['relevance'] == 99:
            non_relevant_data.append(list)
        else:
            relevant_data.append(list)
    data = sorted(relevant_data, key=lambda k: k['relevance'], reverse=False)
    non_relevant_data.reverse()
    for each in non_relevant_data:
        data.append(each)
    return Response({"data": data})

#api for all tabs(tickers)
@csrf_exempt
@api_view(['POST'])
def rec_news_tabs(request):
    chart_type= request.data["chart_type"]
    news_obj = News_rec.objects.all().filter(tab_name = chart_type, archive = 'N')
    data = []
    relevant_data = []
    non_relevant_data = []
    for n in news_obj:
        b = n.date.replace(tzinfo=None)
        a = datetime.datetime.now().replace(microsecond=0)
        # get timedifference for news artticles
        date = a-b
        converted_date=str(date).split(',')
        if len(converted_date)>1:
            if int(converted_date[0].split(' ')[0])<1:
                time=converted_date[1].split(':')[0]+" Hr"
            else:
                time=converted_date[0]
        else:
            if int(converted_date[0].split(':')[0])==0:
                if converted_date[0].split(':')[1]=='00':
                    temp=int(converted_date[0].split(':')[2])
                    time=str(temp) +" sec"
                else:
                    temp=int(converted_date[0].split(':')[1])
                    time=str(temp) + " min"
            else:
                temp=int(converted_date[0].split(':')[0])
                time=str(temp)+" Hr"
        image = n.image
        title = n.title
        id = n.id
        if image == "":
            try:
                first_article = Article(url=n.link, language='en')
                first_article.download()
                first_article.parse()
                image = first_article.top_image
            except:
                image = "https://upload.wikimedia.org/wikipedia/commons/d/d1/Image_not_available.png"
                print("no image found")
            a = News_rec.objects.get(id = id)
            a.image = image
            a.save()
        if title == "":
            try:
                first_article = Article(url=n.link, language='en')
                first_article.download()
                first_article.parse()
                title = first_article.title
            except:
                try:
                    first_article = Article(url=n.link, language='en')
                    first_article.download()
                    first_article.parse()
                    title = first_article.summary
                except:
                    first_article = Article(url=n.link, language='en')
                    first_article.download()
                    first_article.parse()
                    title = first_article.text[:50] + "...."
            a = News_rec.objects.get(id = id)
            a.title = title
            a.save()

        list = {
            "title":n.title,
            "link":n.link,
            "website":n.website,
            "image":image,
            "date":time,
            "relevance": n.relevance_level_tab
        }
        if list['relevance'] == 99:
            non_relevant_data.append(list)
        else:
            relevant_data.append(list)
    data = sorted(relevant_data, key=lambda k: k['relevance'], reverse=False) 
    non_relevant_data.reverse()
    for each in non_relevant_data:
        data.append(each)
    return Response({"data": data})

@api_view(['POST'])
def insert_rec_news(request):
    chart_type= request.data["chart_type"]
    link= request.data["link"]
    website= request.data["website"]
    dateTime= request.data["dateTime"]
    lp_config= request.data["lp_config"]
    lp_rel= request.data["lp_rel"]
    exp_date= request.data["exp_date"]
    paid = request.data["paid"]
    if paid == 1:
        image = request.data["image"]
        title = request.data["title"]
    else:
        # fetch image
        try:
            first_article = Article(url=link, language='en')
            first_article.download()
            first_article.parse()
            image = first_article.top_image
        except:
            image = "https://upload.wikimedia.org/wikipedia/commons/d/d1/Image_not_available.png"
            print("no image found")
        # fetch title
        try:
            first_article = Article(url=link, language='en')
            first_article.download()
            first_article.parse()
            title = first_article.title
        except:
            try:
                first_article = Article(url=link, language='en')
                first_article.download()
                first_article.parse()
                title = first_article.summary
            except:
                first_article = Article(url=link, language='en')
                first_article.download()
                first_article.parse()
                title = first_article.text[:50] + "...."
    
    # landing page check
    if lp_config == 1:
        lp = 'Y'
    else:
        lp = 'N'
    
    for each in chart_type:
        data_obj = News_rec(tab_name = each, on_landing_page = lp, relevance_level_landing_page = lp_rel,  link=link, title = title, website = website, date = dateTime, image = image, archive = 'N', exp_date = exp_date)
        data_obj.save()
        lp = 'N'
        lp_rel = 99

    return Response({"status": 200})

@api_view(['GET'])
def expire_news(request):
    data_obj = News_rec.objects.all()
    d1 = datetime.datetime.today()
    # print(d1)
    for each in data_obj:
        id = each.id
        temp = each.exp_date
        temp_d = temp.strftime("%Y-%m-%d %H:%M:%S")
        d2 = datetime.datetime.strptime(temp_d, "%Y-%m-%d %H:%M:%S")
        # print(d2)
        if d1 >= d2:
            # print("N")
            a = News_rec.objects.get(id = id)
            a.archive = "Y"
            a.save()

    return Response({"status":200})


#############depricated##################

# fetch the data for the reccomended news
# @api_view(['GET'])
# def rec_news_fetch_data(request):
#     news_obj = News_rec.objects.all().filter(archive = 'N')
#     for n in news_obj:
#         image = n.image
#         title = n.title
#         id = n.id
#         website = n.website
#         if image == "":
#             try:
#                 first_article = Article(url=n.link, language='en')
#                 first_article.download()
#                 first_article.parse()
#                 image = first_article.top_image
#             except:
#                 image = "https://upload.wikimedia.org/wikipedia/commons/d/d1/Image_not_available.png"
#                 print("no image found")
#             # a = News_rec.objects.get(link=n.link, tab_name = n.tab_name,  relevance_level_landing_page = n.relevance_level_landing_page, relevance_level_tab = n.relevance_level_tab)
#             a = News_rec.objects.get(id = id)
#             a.image = image
#             a.save()
#         if title == "":
#             try:
#                 first_article = Article(url=n.link, language='en')
#                 first_article.download()
#                 first_article.parse()
#                 title = first_article.title
#             except:
#                 try:
#                     first_article = Article(url=n.link, language='en')
#                     first_article.download()
#                     first_article.parse()
#                     title = first_article.summary
#                 except:
#                     first_article = Article(url=n.link, language='en')
#                     first_article.download()
#                     first_article.parse()
#                     title = first_article.text[:50] + "...."
#             print(title)
#             # a = News_rec.objects.get(link=n.link, tab_name = n.tab_name,  relevance_level_landing_page = n.relevance_level_landing_page, relevance_level_tab = n.relevance_level_tab)
#             a = News_rec.objects.get(id = id)
#             a.title = title
#             a.save()
#         # if website == "":
#         #     website_list = ['ACCESSWIRE', 'American City Business Journals', 'Barrons.com', 'Benzinga', 'Bloomberg', 'Business Wire', 'FX Empire', 'GlobeNewswire', 'Insider Monkey', 'Investing.com', 'Investopedia', "Investor's Business Daily", "Investor's Business Daily Video", 'InvestorPlace', 'MarketWatch', 'MoneyWise', "Moody's", 'Motley Fool', 'Newsfile', 'Oilprice.com', 'PR Newswire', 'Reuters', "Schaeffer's Investment Research", 'Simply Wall St.', 'SmarterAnalyst', 'The Independent', 'The Telegraph', 'The Wall Street Journal', 'TheStreet.com', 'TipRanks', 'Yahoo Finance', 'Yahoo Finance UK', 'Yahoo Finance Video', 'Zacks']
#         #     link = "https://www.businesswire.com/news/home/20221128005524/en/"
#         #     t = urlparse(link).netloc
#         #     website = '.'.join(t.split('.')[-2:])
#         #     website = website.split('.')[0]

#     return Response({"status": 200})
