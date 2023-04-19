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
import requests
from newspaper import Article
from dateutil import parser

# for individual tickers
@api_view(['POST'])
def tweet_data_ticker(request):
    # print(request.data)
    tab_name= request.data["tab_name"]
    tweet_obj = tweet_table_ticker.objects.all().filter(tab_name = tab_name, archive = "N")
    # tweet_obj = tweet_table_ticker_test.objects.all().filter(tab_name = tab_name, archive = "N")
    data = []
    relevant_data = []
    non_relevant_data = []
    for n in tweet_obj:
        try:
            # print(n.tweet_link)
            link = n.tweet_link
            if n.html == "" or n.author_name=="" or n.author_url=="" or n.profile_pic=="":
                url = "https://publish.twitter.com/oembed?url=" + link + "&hide_thread=true&theme=dark&omit_script=true"
                response = requests.request("GET", url, headers={}, data={})
                res = response.text
                res= json.loads(res)
                # html = res["html"]
                author_name = res["author_name"]
                author_url = res["author_url"]
                html = fetch_html(link)
                # a = tweet_table_ticker(tab_name = tab_name, tweet_link = link, html = html)
                n.html = str(html)
                n.author_name = str(author_name)
                n.author_url = str(author_url)
                n.profile_pic = fetch_profile_picture(author_url)
                n.image_url = fetch_image_url(link)
                temp = fetch_weburls_img(link)
                n.web_url = temp[0]
                n.web_url_image = temp[1]
                n.web_text = temp[2]
                n.save()
            html = n.html
            author_name = n.author_name
            author_url = n.author_url
            profile_pic = n.profile_pic
            image_url = n.image_url
            web_url = n.web_url
            web_url_image = n.web_url_image
            web_text = n.web_text
            date = date_format(n.date)
            list = {
                "link":link,
                "html":html,
                "author_name":author_name,
                "author_url":author_url,
                "profile_pic": profile_pic,
                "image_url": image_url,
                "web_url" : web_url,
                "web_url_image" : web_url_image,
                "web_text" : web_text,
                "relevance": n.relevance_level_tab,
                "date":date
            }
            # data.append(list)
            if list['relevance'] == 99:
                non_relevant_data.append(list)
            else:
                relevant_data.append(list)
            # data.sort(key=data['relevance'], reverse=True)
        except:   
            print("tweet doesn't exist")
    data = sorted(relevant_data, key=lambda k: k['relevance'], reverse=False) 
    non_relevant_data.reverse()
    for each in non_relevant_data:
        data.append(each)
    # print(data)
    return Response({"data": data})

# for individual index
@api_view(['POST'])
def tweet_data_index(request):
    # print(request.data)
    chart= request.data["chart"]
    tweet_obj = tweet_table_index.objects.all().filter(chart = chart, archive = "N")
    # tweet_obj = tweet_table_index_test.objects.all().filter(chart = chart, archive = "N")
    data = []
    relevant_data = []
    non_relevant_data = []
    for n in tweet_obj:
        try:
            # print(n.tweet_link)
            link = n.tweet_link
            if n.html == "" or n.author_name=="" or n.author_url=="" or n.profile_pic=="":
                url = "https://publish.twitter.com/oembed?url=" + link + "&hide_thread=true&theme=dark&omit_script=true"
                response = requests.request("GET", url, headers={}, data={})
                res = response.text
                res= json.loads(res)
                # html = res["html"]
                author_name = res["author_name"]
                author_url = res["author_url"]
                html = fetch_html(link)
                # a = tweet_table_ticker(tab_name = tab_name, tweet_link = link, html = html)
                n.html = str(html)
                n.author_name = str(author_name)
                n.author_url = str(author_url)
                n.profile_pic = fetch_profile_picture(author_url)
                n.image_url = fetch_image_url(link)
                temp = fetch_weburls_img(link)
                n.web_url = temp[0]
                n.web_url_image = temp[1]
                n.web_text = temp[2]
                n.save()
            html = n.html
            author_name = n.author_name
            author_url = n.author_url
            profile_pic = n.profile_pic
            image_url = n.image_url
            web_url = n.web_url
            web_url_image = n.web_url_image
            web_text = n.web_text
            date = date_format(n.date)
            list = {
                "link":link,
                "html":html,
                "author_name":author_name,
                "author_url":author_url,
                "profile_pic": profile_pic,
                "image_url": image_url,
                "web_url" : web_url,
                "web_url_image" : web_url_image,
                "web_text" : web_text,
                "relevance": n.relevance_level,
                "date": date
            }
            # data.append(list)
            if list['relevance'] == 99:
                non_relevant_data.append(list)
            else:
                relevant_data.append(list)
            # data.sort(key=data['relevance'], reverse=True)
        except: 
            print("tweet doesn't exist")
    data = sorted(relevant_data, key=lambda k: k['relevance'], reverse=False) 
    non_relevant_data.reverse()
    for each in non_relevant_data:
        data.append(each)
    # print(data)
    return Response({"data": data})

# for landing page
@api_view(['GET'])
def tweet_data_landing(request):
    tweet_obj = tweet_table_ticker.objects.all().filter(on_landing_page = "Y",  archive = 'N')
    # tweet_obj = tweet_table_ticker_test.objects.all().filter(on_landing_page = "Y",  archive = 'N')
    data = []
    relevant_data = []
    non_relevant_data = []
    for n in tweet_obj:
        try:
            # print(n.tweet_link)
            link = n.tweet_link
            if n.html == "" or n.author_name=="" or n.author_url=="" or n.profile_pic=="":
                url = "https://publish.twitter.com/oembed?url=" + link + "&hide_thread=true&theme=dark&omit_script=true"
                response = requests.request("GET", url, headers={}, data={})
                res = response.text
                res= json.loads(res)
                # html = res["html"]
                author_name = res["author_name"]
                author_url = res["author_url"]
                html = fetch_html(link)
                # a = tweet_table_ticker(tab_name = tab_name, tweet_link = link, html = html)
                n.html = str(html)
                n.author_name = str(author_name)
                n.author_url = str(author_url)
                n.profile_pic = fetch_profile_picture(author_url)
                n.image_url = fetch_image_url(link)
                temp = fetch_weburls_img(link)
                n.web_url = temp[0]
                n.web_url_image = temp[1]
                n.web_text = temp[2]
                n.save()
            html = n.html
            author_name = n.author_name
            author_url = n.author_url
            profile_pic = n.profile_pic
            image_url = n.image_url
            web_url = n.web_url
            web_url_image = n.web_url_image
            web_text = n.web_text
            date = date_format(n.date)
            list = {
                "link":link,
                "html":html,
                "author_name":author_name,
                "author_url":author_url,
                "profile_pic": profile_pic,
                "image_url": image_url,
                "web_url" : web_url,
                "web_url_image" : web_url_image,
                "web_text" : web_text,
                "relevance": n.relevance_level_landing_page,
                "date": date
            }
            # data.append(list)
            if list['relevance'] == 99:
                non_relevant_data.append(list)
            else:
                relevant_data.append(list)
            # data.sort(key=data['relevance'], reverse=True)
        except:
            print("tweet doesn't exist")
    data = sorted(relevant_data, key=lambda k: k['relevance'], reverse=False) 
    non_relevant_data.reverse()
    for each in non_relevant_data:
        data.append(each)
    # print(data)
    return Response({"data": data})

@api_view(['GET'])
def twitter_data_fetch(request):
    tweet_obj = tweet_table_ticker.objects.all().filter(archive = 'N')
    # tweet_obj = tweet_table_ticker_test.objects.all().filter(archive = 'N')
    for n in tweet_obj:
        try:
            # print(n.tweet_link)
            link = n.tweet_link
            if n.html == "" or n.author_name=="" or n.author_url=="" or n.profile_pic=="":
                url = "https://publish.twitter.com/oembed?url=" + link + "&hide_thread=true&theme=dark&omit_script=true"
                response = requests.request("GET", url, headers={}, data={})
                res = response.text
                res= json.loads(res)
                # html = res["html"]
                author_name = res["author_name"]
                author_url = res["author_url"]
                html = fetch_html(link)
                # a = tweet_table_ticker(tab_name = tab_name, tweet_link = link, html = html)
                n.html = str(html)
                n.author_name = str(author_name)
                n.author_url = str(author_url)
                n.profile_pic = fetch_profile_picture(author_url)
                n.image_url = fetch_image_url(link)
                temp = fetch_weburls_img(link)
                n.web_url = temp[0]
                n.web_url_image = temp[1]
                n.web_text = temp[2]
                n.save()
        except:
                print("no data")
    
    tweet_obj = tweet_table_index.objects.all().filter(archive = "N")
    # tweet_obj = tweet_table_index_test.objects.all().filter(archive = "N")
    for n in tweet_obj:
        try:
            # print(n.tweet_link)
            link = n.tweet_link
            if n.html == "" or n.author_name=="" or n.author_url=="" or n.profile_pic=="" or n.image_url=="" or n.web_url=="":
                url = "https://publish.twitter.com/oembed?url=" + link + "&hide_thread=true&theme=dark&omit_script=true"
                response = requests.request("GET", url, headers={}, data={})
                res = response.text
                res= json.loads(res)
                # html = res["html"]
                author_name = res["author_name"]
                author_url = res["author_url"]
                html = fetch_html(link)
                # a = tweet_table_ticker(tab_name = tab_name, tweet_link = link, html = html)
                n.html = str(html)
                n.author_name = str(author_name)
                n.author_url = str(author_url)
                n.profile_pic = fetch_profile_picture(author_url)
                n.image_url = fetch_image_url(link)
                temp = fetch_weburls_img(link)
                n.web_url = temp[0]
                n.web_url_image = temp[1]
                n.web_text = temp[2]
                n.save()
        except:
            print("no data")
    return Response({"data":200})


def fetch_profile_picture(url):
    username = url.rsplit('/', 1)[-1]
    url = "https://api.twitter.com/2/users/by/username/"+ username +"?user.fields=profile_image_url"

    payload={}
    headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAIEuWwEAAAAAd5ArTkqfdvISmDuJakqarkIY3%2FM%3Dd82y724vbTeHkNhi1VnfD76gjAeNrFUhvd75qe7YU94nCC3FnN',
    'Cookie': 'guest_id=v1%3A163488269600637289; guest_id_ads=v1%3A163488269600637289; guest_id_marketing=v1%3A163488269600637289; personalization_id="v1_pNF9fHfRhHhDXcWlOt9wCg=="'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.text
    # print(res)
    res= json.loads(res)

    profile_pic = res["data"]["profile_image_url"]
    # print(profile_pic)

    return profile_pic

def fetch_image_url(url):
    id = url.rsplit('/', 1)[-1]
    url = "https://api.twitter.com/2/tweets?ids="+ id +"&expansions=attachments.media_keys&media.fields=url"
    payload={}
    headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAIEuWwEAAAAAd5ArTkqfdvISmDuJakqarkIY3%2FM%3Dd82y724vbTeHkNhi1VnfD76gjAeNrFUhvd75qe7YU94nCC3FnN',
    'Cookie': 'guest_id=v1%3A163488269600637289; guest_id_ads=v1%3A163488269600637289; guest_id_marketing=v1%3A163488269600637289; personalization_id="v1_pNF9fHfRhHhDXcWlOt9wCg=="'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.text
    res= json.loads(res)
    try:
        image_url = res["includes"]["media"][0]["url"]
        # print(image_url)
    except:
        image_url = " "
    return image_url

def fetch_weburls_img(url):
    id = url.rsplit('/', 1)[-1]
    url = "https://api.twitter.com/2/tweets/"+ id +"?tweet.fields=entities"
    payload={}
    headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAIEuWwEAAAAAd5ArTkqfdvISmDuJakqarkIY3%2FM%3Dd82y724vbTeHkNhi1VnfD76gjAeNrFUhvd75qe7YU94nCC3FnN',
    'Cookie': 'guest_id=v1%3A163488269600637289; guest_id_ads=v1%3A163488269600637289; guest_id_marketing=v1%3A163488269600637289; personalization_id="v1_pNF9fHfRhHhDXcWlOt9wCg=="'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.text
    res= json.loads(res)
    # print(res["data"]["entities"])
    try:
        entity = res["data"]["entities"]["urls"][0]
        # print(entity)
        web_url = entity["unwound_url"]
        # print(web_url.rsplit('.', 1)[-1])
        if web_url.rsplit('.', 1)[-1] == "pdf":
            web_url = " "
            web_url_image = " "
            web_text = " "
        else:
            first_article = Article(url=web_url, language='en')
            first_article.download()
            first_article.parse()
            web_text = first_article.title
            web_url_image = first_article.top_image
    except:
        web_url = " "
        web_url_image = " "
        web_text = " "
    return([web_url, web_url_image, web_text])

def fetch_html(url):
    id = url.rsplit('/', 1)[-1]
    url = "https://api.twitter.com/2/tweets/"+id+"?tweet.fields=created_at"
    payload={}
    headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAIEuWwEAAAAAd5ArTkqfdvISmDuJakqarkIY3%2FM%3Dd82y724vbTeHkNhi1VnfD76gjAeNrFUhvd75qe7YU94nCC3FnN',
    'Cookie': 'guest_id=v1%3A163488269600637289; guest_id_ads=v1%3A163488269600637289; guest_id_marketing=v1%3A163488269600637289; personalization_id="v1_pNF9fHfRhHhDXcWlOt9wCg=="'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.text
    res = json.loads(res)
    # print(res)
    text = res["data"]["text"]
    return(text)

def fetch_date(url):
    id = url.rsplit('/', 1)[-1]
    url = "https://api.twitter.com/2/tweets/"+id+"?tweet.fields=created_at"
    payload={}
    headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAIEuWwEAAAAAd5ArTkqfdvISmDuJakqarkIY3%2FM%3Dd82y724vbTeHkNhi1VnfD76gjAeNrFUhvd75qe7YU94nCC3FnN',
    'Cookie': 'guest_id=v1%3A163488269600637289; guest_id_ads=v1%3A163488269600637289; guest_id_marketing=v1%3A163488269600637289; personalization_id="v1_pNF9fHfRhHhDXcWlOt9wCg=="'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.text
    res = json.loads(res)
    date = res["data"]["created_at"]
    date = parser.isoparse(date)
    # date_temp = date.strftime("%I:%M %p • %b %d, %Y")
    date_temp = date.strftime("%Y-%m-%d %H:%M:%S")
    # print(date_temp)
    return(date_temp)

def date_format(date):
    # print(type(date))
    # print(date)
    b = date.replace(tzinfo=None)
    # print("b--> ",b)
    a = datetime.datetime.now().replace(microsecond=0)
    # print("a--> ",a)
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
    # print(time)
    time = time + " ago"
    return(time)


@api_view(['GET'])
def twitter_data_fetch_test(request):
    tweet_obj = tweet_table_ticker_test.objects.all().filter(archive = 'N')
    for n in tweet_obj:
        try:
            link = n.tweet_link
            if n.html == "":
                print(link)
                url = "https://publish.twitter.com/oembed?url=" + link + "&hide_thread=true&theme=dark&omit_script=true"
                response = requests.request("GET", url, headers={}, data={})
                res = response.text
                res= json.loads(res)
                author_name = res["author_name"]
                author_url = res["author_url"]
                html = fetch_html(link)
                n.html = str(html)
                n.author_name = str(author_name)
                n.author_url = str(author_url)
                n.profile_pic = fetch_profile_picture(author_url)
                n.image_url = fetch_image_url(link)
                temp = fetch_weburls_img(link)
                n.web_url = temp[0]
                n.web_url_image = temp[1]
                n.web_text = temp[2]
                n.save()
        except:
            print("no data")
        
    tweet_obj = tweet_table_index_test.objects.all().filter(archive = "N")
    for n in tweet_obj:
        try:
            print(n.tweet_link)
            link = n.tweet_link
            if n.html == "":
                url = "https://publish.twitter.com/oembed?url=" + link + "&hide_thread=true&theme=dark&omit_script=true"
                response = requests.request("GET", url, headers={}, data={})
                res = response.text
                res= json.loads(res)
                author_name = res["author_name"]
                author_url = res["author_url"]
                html = fetch_html(link)
                n.html = str(html)
                n.author_name = str(author_name)
                n.author_url = str(author_url)
                n.profile_pic = fetch_profile_picture(author_url)
                n.image_url = fetch_image_url(link)
                temp = fetch_weburls_img(link)
                n.web_url = temp[0]
                n.web_url_image = temp[1]
                n.web_text = temp[2]
                n.save()
        except:
            print("no data")
    return Response({"data": 200})