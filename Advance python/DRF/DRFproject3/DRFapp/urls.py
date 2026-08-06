from django.urls import path
from . import views

urlpatterns = [
 path('addlaptop/', views.AddLaptop, name='addlaptop'),
 path('getlaptop/<str:laptop_id>/', views.GetLaptop, name='getlaptop'),
 path('updatelaptop/<str:laptop_id>/', views.UpdateLaptop, name='updatelaptop'),
 path('deletelaptop/<str:laptop_id>/', views.DeleteLaptop, name='deletelaptop'),
 path('showalllaptop/', views.ShowAllLpatop, name='showalllaptop'),
]