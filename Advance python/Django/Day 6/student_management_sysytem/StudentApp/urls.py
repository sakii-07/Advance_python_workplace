from django.urls import path
from . import views
urlpatterns = [
    path('getregistrationpage/', views.GetRegistrationPage, name='getregistrationpage'),
    path('register/', views.Register, name='register'),

    path('navbar/', views.Navbar, name='navbar'),
    path('showallstudents/', views.ShowAllStudents, name='showallstudents'),

    path('getupdatepage/', views.GetUpdatePage, name='getupdatepage'),
    path('showstudentforupdate/', views.ShowStudentForUpdate, name='showstudentforupdate'),
    path('update/', views.Update, name='update'),
    path('updateforshowall/<str:username>', views.UpdateForShowAll, name='updateforshowall'),

    path('deletestudentsforshowall/<str:username>', views.DeleteStudentForShowall,name='deletestudentsforshowall'),
    path('getdeletepage/',views.GetDeletePage, name='getdeletepage'),
    path('delete/', views.Delete, name='delete'),

    path('logout/', views.Logout, name='logout'),

    path('loginstudent/',views.LoginStudent, name='loginstudent'),
    path('', views.GetLoginPage, name='getloginpage'),

    path('signin/', views.SignIn,name='signin'),
    path('getsigninpage/', views.GetSigninPage, name='getsigninpage'),
]