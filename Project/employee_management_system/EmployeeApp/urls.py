from . import views
from django.urls import path

urlpatterns = [
   path("", views.Dashboard, name='dashboard'),
   path('addemployee/', views.AddEmployee, name='addemployee'),
   path("showemployee/", views.ShowEmployees, name="showemployee"),
   path("deleteemployee/<str:empId>/", views.DeleteEmployee, name='deleteemployee'),
   path('updateemployee/<str:empId>/', views.UpdateEmployee, name='updateemployee'),
   path('getupdateemployeepage/<str:empId>/', views.GetUpdateEmployeePage, name='getupdateemployeepage'),
]
