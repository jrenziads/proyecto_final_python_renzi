from django.views.generic import TemplateView, CreateView, ListView, FormView
from django.urls import reverse_lazy
from .forms import BrandForm, CarForm, OwnerForm, SearchForm
from .models import Car

class IndexView(ListView):
    model = Car
    template_name = 'web_autos/index.html'
    context_object_name = 'cars'

    def get_queryset(self):
        queryset = super().get_queryset()
        brand = self.request.GET.get('brand')
        model = self.request.GET.get('model')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        if brand:
            queryset = queryset.filter(brand__name__icontains=brand)
        if model:
            queryset = queryset.filter(model__icontains=model)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset

class AboutView(TemplateView):
    template_name = 'web_autos/about.html'

class AddBrandView(CreateView):
    form_class = BrandForm
    template_name = 'web_autos/add_brand.html'
    success_url = reverse_lazy('index')

class AddCarView(CreateView):
    form_class = CarForm
    template_name = 'web_autos/add_car.html'
    success_url = reverse_lazy('index')

class AddOwnerView(CreateView): 
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
