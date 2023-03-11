from django.urls import path

from . import views

app_name = 'themovie'

urlpatterns = [
    path('discover_movie/', views.discover_all_movie,  name='Movie Discover'),
    path('discover_tv/', views.discover_tv_details,  name='TV Discover'),

    path('find/<int:external_id>', views.find_movie,  name='Find Movie, TV'),


    path('tv/', views.genre_tv_list,  name='Genre TV List'),
    path('tv/<int:tv_id>', views.get_tv_details,  name='Get TV Details'),
    path('tv/<int:tv_id>/account_state', views.get_tv_account_state,  name='Get TV Account Details'),
    path('tv/<int:tv_id>/credits', views.get_tv_credits,  name='Get TV Credits'),
    path('tv/<int:tv_id>/reviews', views.get_tv_reviews,  name='Get TV Reviews'),
    path('tv/<int:tv_id>/videos', views.get_tv_videos,  name='Get TV Videos'),
    path('popular_tv/', views.get_popular_tv,  name='Get Popular TV Shows'),
    path('top_rated_tv/', views.get_top_rated_tv,  name='Get Top RatednTV Shows'),


    path('movie/', views.genre_movie_list,  name='Genre Movie List'),
    path('movie/<int:movie_id>/<int:page_number>', views.get_movie_id,  name='Movie ID'),
    path('movie/<int:movie_id>/credits', views.get_movie_credit,  name='Movie Credits'),

    path('list/', views.create_list,  name='Create List'),
    path('list/<int:list_id>', views.get_list,  name='Get List'),
    path('list/<int:list_id>/status', views.get_list_item_status,  name='Get List Item Status'),

    path('trending/', views.get_trending,  name='Get Trending'),
    path('review/<int:review_id>', views.get_movie_review,  name='Get Movie Review'),

    path('search_company/', views.search_company,  name='Search Company'),
    path('search_collection/', views.search_collection,  name='Search Collection'),


]
