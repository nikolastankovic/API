from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import requests
from django.views.decorators.csrf import ensure_csrf_cookie

from django.http import JsonResponse
from django.core import serializers

from .serializers import FileSerializer
from django.views.decorators.csrf import csrf_exempt

import json
import time

@ensure_csrf_cookie
def send_json(request):
    if request.method == "POST":
      
        first_name = request.POST.get('username')
        IP = request.POST.get('ip')

       # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
       # ip = request.META.get('REMOTE_ADDR')

      
        url = 'https://vsrequest.video/request.php?key=frSQnQ6ck5CIl5t4&secret_key=sdyebvzptylnjl5s06ukz7kurjis31&video_id='+first_name+'&ip='+IP
        x = requests.get(url)
        
       
        ticket = x.text

    
        
        
        
        data12 = [{'name': first_name, 'ticket': ticket}]


    return JsonResponse(data12,safe=False)

def search_episodes(request):
    if request.method == 'POST':
        episodeid = request.POST.get('episodeid')
        ES = request.POST.get('sezona')
        IP = request.POST.get('ip')
        EE = request.POST.get('ee')
        url = 'https://vsrequest.video/request.php?key=frSQnQ6ck5CIl5t4&secret_key=sdyebvzptylnjl5s06ukz7kurjis31&video_id='+episodeid+'&tv=1&s='+ES+'&ip='+IP+'&e='+EE

        ticket_episode = requests.get(url)
        
        ticket_episode_text = ticket_episode.text + '&e=' + EE
        print(ticket_episode_text)
        print(episodeid)
        print(ES)
        print(IP)
        print(EE)
        episode_data = [{'ticket':ticket_episode_text,'name':episodeid}]
        print(episode_data)
        print(url)
    
    return JsonResponse(episode_data,safe=False)


def search_movie(request):
    if request.method == 'POST':

        search = request.POST.get('search')
        url2 = 'http://www.omdbapi.com/?s='+search+'&apikey=9ff0e32f'
        movies = requests.get(url2)
        resp = movies.json()

    return JsonResponse(resp,safe=False)




    

      
    



  

    