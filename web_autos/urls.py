from django.urls import path
from .views import IndexView, AddBrandView, AddCarView, AddOwnerView, SearchView, AboutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('add_brand/', AddBrandView.as_view(), name='add_brand'),
    path('add_car/', AddCarView.as_view(), name='add_car'),
    path('add_owner/', AddOwnerView.as_view(), name='add_owner'), 
    path('search/', SearchView.as_view(), name='search'),
]
