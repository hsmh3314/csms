from django.urls import path
from . import views

app_name = 'csms'

urlpatterns = [
    path('', views.index, name='index'),
    path('service/', views.service_index, name='service_index'),
    path('service/detail/<int:service_sNo>/', views.service_detail, name='service_detail'),
    path('service/create/', views.service_create, name='service_create'),
    path('customer/detail/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('customer/create/', views.customer_create, name='customer_create'),
    path('customer/modify/<int:customer_id>/', views.customer_modify,
         name='customer_modify'),
    path('customer/delete/<int:customer_id>/', views.customer_delete,
         name='customer_delete'),
]