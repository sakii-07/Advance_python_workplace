from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetCheckCustomerPage, name='GetCheckCustomerPage'),
    path('checkcustomer/', views.CheckCustomer, name='checkcustomer')
]