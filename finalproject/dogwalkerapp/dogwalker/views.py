from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Service


class ServiceView(ListView):
    model = Service
    template_name = 'dogwalker/service_index.html'
    context_object_name = 'service'

    def get_context_data(self, *args, **kwargs):
        data = super(ServiceView, self).get_context_data(*args, **kwargs)
        return data


class ServiceDetailView(DetailView):

    model = Service
    template_name = 'dogwalker/service_detail.html'


class CreateServiceView(CreateView):

    model = Service
    fields = ['name']
    template_name = 'dogwalker/service_index.html'
