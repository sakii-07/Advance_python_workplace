from django.urls import path
from . import views

urlpatterns = [
    path('getsignuppage/',views.GetSignUpPage, name='getsignuppage'),
    path('signup/', views.SignUp, name='signup'),

    path('getloginpage/',views.GetLoginPage, name='getloginpage'),
    path('login/', views.Login, name='login'),

    path('getnavbar/', views.GetNavbar, name='navbar'),
    path('gethomepage/', views.GetHomePage, name='homepage'),

    path('getaddmedicinepage/', views.GetAddMedicinePage, name='getmedicinepage'),
    path('addmedicine/', views.AddMedicine, name='addmedicine'),

    path('getviewmedicinepage/', views.GetViewMedicinePage, name='viewallmed'),
    path('viewmadpage/', views.ViewMedPage, name='viewmed'),

    path('updatemedpage/<int:id>/', views.GetUpdateMedPage, name='updatemedpage'),
    path('updatemedicine/', views.UpdateMed, name='updatemedicine'),

    path('deletemedicine/<int:id>/', views.DeleteMedicine, name='deletemedicine'),

    path('getcategoriespage/', views.GetCategoriesPage, name='categories'),
    path('gethealthcarepage/', views.GethealthcaePage, name='gethealthcarepage'),
    path('getaboutpage/', views.GetaboutPage, name='getaboutpage'),
    path('logout/', views.Logout, name='logout'),
    


]