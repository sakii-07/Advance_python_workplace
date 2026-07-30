from django.urls import path, include
from . import views

urlpatterns = [
    path('getsigninpage/', views.GetSigninPage, name='getsigninpage'),
    path('signin/', views.Signin, name='signin'),

    path('', views.GetLoginPage, name='getloginpage'),
    path('login/', views.Login, name='login'),

    path('getnavbar/', views.GetNavbar, name='getnavbar'),
    path('gethomepage/', views.GetHomePage, name='gethomepage'),

    path('logout/', views.Logout,name="logout"),

    path('getproductformpage/', views.GetProductFormPage, name='getproductformpage'),
    path('getshowallproductpage/', views.ShowProductsPage, name='getshowallproductpage'),

    path('addproducts/', views.AddProduct, name='addproducts'),

    path('updateproduct/',views.UpdateProduct, name='updateproduct'),
    path('getupdateproductpage/<str:product_name>/', views.GetUpdateProductPage, name='getupdateproductpage'),

    path('deleteproduct/<str:product_name>/', views.DeleteProduct, name='deleteproduct'),

    path('getupdateuserdetailspage/<str:username>/', views.GetUpdateUserDetailsPage, name='getupdateuserdetailspage'),
    path('userdetails/', views.UserDetails, name='userdetails'),
    path('updateuserdetails/', views.UpdateUserDetails, name='updateuserdetails'),
    path('getuserdetailspage/', views.GetUserDetailsPage, name='getuserdetailspage'),

    path('getcategoryspage/', views.GetCategoryPage, name='getcategoryspage'),
    path('getaboutpage/', views.GetAboutPage, name='getaboutpage'),
    path('getcontactpage/', views.GetContactPage, name='getcontactpage'),

]