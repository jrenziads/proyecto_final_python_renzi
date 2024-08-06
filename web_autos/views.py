from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, FormView
from .forms import BrandForm, CarForm, OwnerForm, SearchForm
from .models import Brand, Car, Owner

class IndexView(ListView):
    model = Car
    template_name = 'web_autos/index.html'
    context_object_name = 'cars'

class AddBrandView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'web_autos/add_brand.html'
    success_url = reverse_lazy('index')

class AddCarView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'web_autos/add_car.html'
    success_url = reverse_lazy('index')

class AddOwnerView(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'web_autos/add_owner.html'
    success_url = reverse_lazy('index')

class SearchView(FormView):
    form_class = SearchForm
    template_name = 'web_autos/search.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Car.objects.filter(model__icontains=query)
            return self.render_to_response(self.get_context_data(form=form, results=results))
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        query = form.cleaned_data['query']
        results = Car.objects.filter(model__icontains=query)
        return self.render_to_response(self.get_context_data(form=form, results=results))

