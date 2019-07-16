from django.urls import path
from django.urls import include, re_path
from . import views
from restaurant.views import (ContactView, AboutTemplateView, 
restaurant_listview, RestaurantListView, RestaurantDetailtView,
restaurant_createview)


urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('restaurant/', views.restaurant_listview, name='restaurant-list'),
    path('restaurant/create/', views.restaurant_createview, name='restaurant-form'),
]

urlpatterns += [
    # re_path(r'^restaurant/(?P<slug>\w+)/$', RestaurantListView.as_view()),
    re_path(r'restaurant/(?P<slug>[\w-]+)/$', RestaurantDetailtView.as_view(), name='restaurant-detail'),
]
