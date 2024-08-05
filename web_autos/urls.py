from django.urls import path
from .views import index, add_brand, add_car, add_owner, search

urlpatterns = [
    path('', index, name='index'),
    path('add_brand/', add_brand, name='add_brand'),
    path('add_car/', add_car, name='add_car'),
    path('add_owner/', add_owner, name='add_owner'),
    path('search/', search, name='search'),
]
