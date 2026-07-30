from django.urls import path
from . import views 

urlpatterns = [
    path('addstudent/', views.AddStudent, name='addstudent'),
    path('getstudent/<str:rollno>/', views.GetStudent, name='getstudent'),
    path('updatestudent/<str:rollno>/', views.UpdateStudent, name='updatestudent'),
    path('deletestudent/<str:rollno>/', views.DeleteStudent, name='deletestudent')
]
