from django.urls import path, include

from aplicatie1 import admin, views

urlpatterns = [
    # path('admin')
    # path('', include('aplicatie1.urls')),
    path('', include('django.contrib.auth.urls'), {'next_page': '/'}, name='login'),
    path('services/', include('aplicatie1.urls')),
    path('order/', include('aplicatie1.urls')),
    path('', views.IndexView.as_view(), name='index'),
    # path()
    ]