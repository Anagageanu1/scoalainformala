from django.urls import path

from . import views

app_name = 'aplicatie1'

urlpatterns = [
    path("", views.ServiceView.as_view(), name='list_service'),
    path('<int:pk>/', views.ServiceDetailView.as_view(), name='detail_service'),
    path('add/', views.CreateServiceView.as_view(), name='add_service'),
    path('<int:pk>/update/', views.UpdateServiceView.as_view(), name='update_service'),
    path('add/', views.CreateOrderView.as_view(), name='add_order'),
    path('', views.OrderView.as_view(), name='list_order'),
    path('<int:pk>/update/', views.UpdateOrderView.as_view(), name='modify_order'),
    path('<int:pk>/delete/', views.DeleteServiceView.as_view(), name='delete_service'),
    # path('<int:pk>/delete/', views.DeleteServiceView.as_view(), name='delete_order'),
    # path('<str:type>/filter/', views.ServiceFilterView.as_view(), name='service_filter'),
    path('filter/<str:type>', views.ServiceFilterView.as_view(), name='service_filter'),
    # path('filter/<str:type>', views.ServiceFilterView.as_view(), name='service_filter'), de modificat in structura asta la toate


    ]