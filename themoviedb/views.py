from django.shortcuts import render

# Create your views here.
import os
import json
import requests

from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from .models import ListItem


API_KEY = "fc5462f5a436d1d6139b13070b1d3d03"


base_url = 'https://api.themoviedb.org/3'


discover_movie_url = f'/discover/movie?api_key={API_KEY}'
discover_tv_url = f'/discover/tv?api_key={API_KEY}'
genre_movie_url = f'/genre/movie/list?api_key={API_KEY}'
genre_tv_url = f'/genre/tv/list?api_key={API_KEY}'
trending_url = f'/trending/all/day?api_key={API_KEY}'




def discover_all_movie(request):
    movie_url = base_url+discover_movie_url

    if request.method == "GET":
        try:
            my_request = requests.get(movie_url)
            if my_request.ok:
                parse_data = my_request.json()
                return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
            else:
                return HttpResponse(my_request.status_code)
        except:
            return HttpResponse('Exception Occured')


def discover_tv_details(request):
    movie_url = base_url+discover_tv_url
    try:
        my_request = requests.get(movie_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(my_request.status_code)
    except:
        return HttpResponse('Exception Occured')


def find_movie(requests, external_id):
    find_url = base_url+'/find/{external_id}?api_key='+API_KEY

    try:
        my_request = requests.get(find_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse( my_request.status_code)
    except:
        return HttpResponse('Exception Occured')


def genre_movie_list(request):
    genre_url = base_url+genre_movie_url
    try:
        my_request = requests.get(genre_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(my_request.status_code)
    except:
        return HttpResponse('Exception Occured')


def genre_tv_list(request):
    genre_url = base_url+genre_tv_url
    try:
        my_request = requests.get(genre_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(my_request.status_code)
    except:
        return HttpResponse('Exception Occured')


def get_movie_id(request, movie_id, page_number):
    movie_id_url = base_url+f'/movie/{movie_id}?api_key={API_KEY}&page={page_number}'
    try:
        my_request = requests.get(movie_id_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(my_request.status_code)
    except:
        return HttpResponse('Exception Occured')


def get_movie_credit(request, movie_id):
    movie_credit_url = base_url+'/movie/{movie_id}/credits?api_key='+API_KEY
    try:
        my_request = requests.get(movie_credit_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse('Status Code: >> '+my_request.status_code)
    except:
        return HttpResponse('Exception Occured')



def get_list(request, list_id):
    list_url = base_url+'/list/{list_id}?api_key='+API_KEY
    try:
        my_request = requests.get(list_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse('Status Code: >> '+my_request.status_code)
    except:
        return HttpResponse('Exception Occured')


def get_list_item_status(request, list_id):
    list_item_url = base_url+'/list/{list_id}/item_status?api_key='+API_KEY
    try:
        my_request = requests.get(list_item_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse('Status Code: >> '+my_request.status_code)
    except:
        return HttpResponse('Exception Occured')


def get_trending(request):
    trend_url = base_url+trending_url
    try:
        my_request = requests.get(trend_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(my_request.status_code)
    except:
        return HttpResponse('Exception Occured')
