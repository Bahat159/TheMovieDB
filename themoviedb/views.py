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
popular_tv = f'/tv/popular?api_key={API_KEY}'
top_rated_tv = f'/tv/top_rated?api_key={API_KEY}'
search_url = f'/search/company?api_key={API_KEY}'
collection_url = f'/search/collection?api_key={API_KEY}'
keyword_url = f'/search/keyword?api_key={API_KEY}'
search_movie_url = f'/search/movie?api_key={API_KEY}'




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
    finder_url = base_url+f'/find/{external_id}?api_key={API_KEY}'
    try:
        my_request = requests.get(finder_url)
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

def get_tv_account_state(request, tv_id):
    tv_acc_url = base_url+f'/tv/{tv_id}/account_states?api_key={API_KEY}'
    try:
        my_request = requests.get(tv_acc_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(my_request.status_code)
    except:
        return HttpResponse('Exception Occured')


def get_tv_details(request, tv_id):
    get_tv_url = base_url+f'/tv/{tv_id}?api_key={API_KEY}'
    try:
        my_request = requests.get(get_tv_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(my_request.status_code)
    except:
        return HttpResponse('Exception Occured')


def get_tv_credits(request, tv_id):
    tv_credit_url = base_url+f'/tv/{tv_id}/credits?api_key={API_KEY}'
    try:
        my_request = requests.get(tv_credit_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(my_request.status_code)
    except:
        return HttpResponse('Exception Occured')

def get_tv_reviews(request, tv_id):
    tv_review_url = base_url+f'/tv/{tv_id}/reviews?api_key={API_KEY}'
    try:
        my_request = requests.get(tv_review_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(my_request.status_code)
    except:
        return HttpResponse('Exception Occured')


def get_tv_videos(request, tv_id):
    tv_videos_url = base_url+f'/tv/{tv_id}/videos?api_key={API_KEY}'
    try:
        my_request = requests.get(tv_videos_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(my_request.status_code)
    except:
        return HttpResponse('Exception Occured')


def get_popular_tv(request):
    popular_tv_url = base_url+popular_tv
    try:
        my_request = requests.get(popular_tv_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(my_request.status_code)
    except:
        return HttpResponse('Exception Occured')


def get_top_rated_tv(request):
    top_rated_tv_url = base_url+top_rated_tv
    try:
        my_request = requests.get(top_rated_tv_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(my_request.status_code)
    except:
        return HttpResponse('Exception Occured')


def get_movie_id(request, movie_id):
    movie_id_url = base_url+f'/movie/{movie_id}?api_key={API_KEY}'
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
    movie_credit_url = base_url+f'/movie/{movie_id}/credits?api_key={API_KEY}'
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
    list_url = base_url+f'/list/{list_id}?api_key={API_KEY}'
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
    list_item_status_url = base_url+f'/list/{list_id}/item_status?api_key={API_KEY}'
    try:
        my_request = requests.get(list_item_status_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse('Status Code: >> '+my_request.status_code)
    except:
        return HttpResponse('Exception Occured')


def create_list(request):
    list_item_url = base_url+f'/list/?api_key={API_KEY}'

    try:
        """
        list_curator = ListItem(name="Test Data", description="List Item Creation", language="English")
        list_curator.save()
        if list_curator:
            print('Success saving record to db')
        """
        listcurator = {"name": "myname","description": "my description","language": "my language"}
        my_request = requests.post(list_item_url, data=listcurator)
    
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


def get_movie_review(request, review_id):
    review_url = base_url+f'/review/{review_id}?api_key={API_KEY}'
    try:
        my_request = requests.get(review_url)
        print(my_request)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(my_request.status_code)
    except:
        return HttpResponse('Exception Occured')


def search_company(request):
    search_company_url = base_url+search_url
    try:
        my_request = requests.get(search_company_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(my_request.status_code)
    except:
        return HttpResponse('Exception Occured')


def search_collection(request):
    search_collection_url = base_url+collection_url
    try:
        my_request = requests.get(search_collection_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(my_request.status_code)
    except:
        return HttpResponse('Exception Occured')


def search_keyword(request):
    search_keyword_url = base_url+keyword_url
    try:
        my_request = requests.get(search_keyword_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(my_request.status_code)
    except:
        return HttpResponse('Exception Occured')


def search_movie(request):
    search_mo_url = base_url+search_movie_url
    try:
        my_request = requests.get(search_mo_url)
        if my_request.ok:
            parse_data = my_request.json()
            return JsonResponse(parse_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(my_request.status_code)
    except:
        return HttpResponse('Exception Occured')
