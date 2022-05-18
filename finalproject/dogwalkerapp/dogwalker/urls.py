from django.urls import path


app_name = 'dogwalker'

urlpatterns = [
    path("", views.ServiceView.as_view(), name='listare'),
    path('<int>:pk>/', views.ServiceDetailView.as_view(), name='detalii'),

]
