from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from .models import Service, Order


class ServiceView(ListView):
    model = Service
    template_name = 'aplicatie1/service_index.html'
    context_object_name = 'service_list'

    def get_context_data(self, *args, **kwargs):
        data = super(ServiceView, self).get_context_data(*args, **kwargs)
        return data

    def post(self, request):
       return None
    #pe pagina de list (services) vrem sa adaugam un buton in dreptul fiecarui serviciu de pe care vrem sa cream un order => or


class ServiceDetailView(DetailView):

    model = Service
    template_name = 'aplicatie1/service_detail.html'
    context_object_name = "service"

    # def get_context_data(self, *args, **kwargs):
    #     data = super(ServiceDetailView, self).get_context_data(*args, **kwargs)
    #     return data


class IndexView(View):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CreateServiceView(CreateView):

    model = Service
    fields = ['name', 'description', 'price', "type"]
    template_name = 'aplicatie1/service_add.html'

    def get_success_url(self):
        return reverse('aplicatie1:list_service')


class UpdateServiceView(UpdateView):
    model = Service
    fields = ['name','description','price','type']
    template_name = 'aplicatie1/service_update.html'

    def get_success_url(self):
        return reverse('aplicatie1:list_service')


class DeleteServiceView(DeleteView):
    model = Service
    # success_url = '/services/'
    success_url = reverse_lazy('aplicatie1:list_service')



    # def get(self, request, *args, **kwargs):
    #     return self.post(*args, **kwargs)


class OrderView(ListView):
    model = Order
    template_name = 'aplicatie1/order_index.html'
    context_object_name = 'order_service'

    def get_context_data(self, *args, **kwargs):
        data = super(OrderView, self).get_context_data(*args, **kwargs)
        return data

class CreateOrderView(CreateView):
    model = Order
    fields = ["service_id", "order_date"] #de optimizat user id
    template_name = 'aplicatie1/order_detail.html'

    def get_success_url(self):
        return reverse('order:listare')



class UpdateOrderView(UpdateView):
    model = Order
    fields = ["service_id"]
    template_name = 'aplicatie1/order_detail.html'

    def get_success_url(self):
        return reverse('order:listare')


def delete_order(request, pk):
    return redirect('order:listare')


# class ServiceFilterView(DetailView):
#     model = Service
#     template_name = 'aplicatie1/service_filter.html'
#     context_object_name = 'service_list'
#
#     def get_context_data(self, *args, **kwargs):
#         context_data = super(ServiceFilterView, self).get_context_data()
#         material_pk = self.args.get('type', None)
#         f = ServiceFilterView(self.request.GET, queryset=Service.objects.filter(material=material_pk))
#         context_data['services'] = f
#         return context_data

class ServiceFilterView(ListView):
    model = Service
    template_name = 'aplicatie1/service_filter.html'
    context_object_name = 'service_list'

    def get_queryset(self):
        # self.services = get_object_or_404(Service, type=self.kwargs['type'])
        return Service.objects.filter(type=self.kwargs["type"])


    # def get_context_object_data(self, *args, **kwargs):
    #     context = super(ServiceFilterView, self).get_context_data(**args)
    #     context['services'] = Service.objects.all().filter(type='dog_walker')
    #     # context.update({
    #     #     'services': Service.objects.all().filter(type=self.kwargs.get("type"))
    #     # })
    #     # print("context=",  context)
    #     return context

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(ServiceFilterView, self).get_context_data(**kwargs)
    #     # Add in the publisher
    #     context['services'] = self.services
    #     return context

