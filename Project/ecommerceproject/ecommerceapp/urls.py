from django.urls import path
from . import views

urlpatterns = [
    path('addproduct/' , views.AddProduct, name='addproduct'),
    path('getproduct/<int:product_id>/', views.GetProduct, name='getproduct'),
    path('updateproduct/<int:product_id>/', views.UpdateProduct, name='updateproduct'),
]

