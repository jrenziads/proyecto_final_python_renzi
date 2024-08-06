from django.contrib.auth.views import LoginView as AuthLoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserLoginForm
from web_autos.models import Car
from web_autos.forms import CarForm

class LoginView(AuthLoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

class CarListView(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'web_autos/car_list.html'
    context_object_name = 'cars'

class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = 'web_autos/car_form.html'
    success_url = reverse_lazy('car_list')

class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'web_autos/car_form.html'
    success_url = reverse_lazy('car_list')

class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'web_autos/car_confirm_delete.html'
    success_url = reverse_lazy('car_list')
