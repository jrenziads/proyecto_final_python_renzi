from django.urls import path
from .views import IndexView, AddBrandView, AddCarView, AddOwnerView, SearchView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add_brand/', AddBrandView.as_view(), name='add_brand'),
    path('add_car/', AddCarView.as_view(), name='add_car'),
    path('add_owner/', AddOwnerView.as_view(), name='add_owner'),
    path('search/', SearchView.as_view(), name='search'),
]
