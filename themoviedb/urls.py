from django.urls import path

from . import views

app_name = 'themovie'

urlpatterns = [
    path('discover_movie/', views.discover_all_movie,  name='Movie Discover'),
    path('discover_tv/', views.discover_tv_details,  name='TV Discover'),

    path('find/<int:external_id>', views.find_movie,  name='Find Movie, TV'),


    path('tv/', views.genre_tv_list,  name='Genre TV List'),

    path('movie/', views.genre_movie_list,  name='Genre Movie List'),
    path('movie/<int:movie_id>/<int:page_number>', views.get_movie_id,  name='Movie ID'),
    path('movie/<int:movie_id>/credits', views.get_movie_credit,  name='Movie Credits'),

    path('list/<int:list_id>', views.get_list,  name='Get List'),
    path('list/<int:list_id>/status', views.get_list_item_status,  name='Get List Item Status'),

    path('trending/', views.get_trending,  name='Get Trending'),


]
