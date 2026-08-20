from django.urls import path
from . import views
urlpatterns = [
    path('addproduct/', views.AddProduct, name='addproduct'),
    path('updateproduct/<int:product_id>/', views.UpdateProduct, name='updateproduct'),
    path('showallproducts/', views.ShowAllProducts, name='showallproducts'),
    path('getproduct/<int:product_id>/', views.GetProduct, name='getproduct'),
    path('deleteproduct/<int:product_id>/', views.DeleteProduct, name='deleteproduct')
]