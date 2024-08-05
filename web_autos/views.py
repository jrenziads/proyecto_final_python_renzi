from django.shortcuts import render, redirect
from .forms import BrandForm, CarForm, OwnerForm, SearchForm
from .models import Brand, Car, Owner

def index(request):
    cars = Car.objects.all()
    return render(request, 'web_autos/index.html', {'cars': cars})

def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BrandForm()
    return render(request, 'web_autos/add_brand.html', {'form': form})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CarForm()
    return render(request, 'web_autos/add_car.html', {'form': form})

def add_owner(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OwnerForm()
    return render(request, 'web_autos/add_owner.html', {'form': form})


def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Car.objects.filter(model__icontains=query) 
            return render(request, 'web_autos/search.html', {'form': form, 'results': results})
    else:
        form = SearchForm()
    return render(request, 'web_autos/search.html', {'form': form})

