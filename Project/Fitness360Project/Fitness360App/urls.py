from django.urls import path
from . import views

urlpatterns = [
    path('getdashboardpage/', views.GetDashboardPage, name='getdashboardpage'),

    path('getregisterpage/', views.GetRegisterPage, name='getregisterpage'),
    path('register', views.Register, name='register'),

    path('getloginpage/', views.GetLoginPage, name='getloginpage'),
    path('', views.Login, name='login'),

    path('getmyprofilepage/', views.GetMyprofilePage, name='getmyprofilepage'),
    path('updateprofile/', views.UpdateProfile, name='updateprofile'),
    path('getupdateprofilepage/', views.GetUpdateProfilePage, name='getupdateprofilepage'),

    path('logout/', views.Logout, name='logout'),

    path('showalltrainers/', views.ShowAllTrainers, name='showalltrainers'),
    path('getaddtrainerpage/', views.GetAddTrainerPage, name='getaddtrainerpage'),
    path('addtrainer/', views.AddTrainer, name='addtrainer'),
    path('getupdatetrainerpage/<str:trainer_id>/', views.GetUpdateTrainerPage, name='getupdatetrainerpage'),

    path('showallequipmnts/', views.ShowAllEquipmnts, name='showallequipmnts'),
    path('addequipment/', views.AddEquipment, name='addequipment'),
    path('getupdateequipmentpage/<str:equipment_id>/', views.GetUpdateEquipmentPage, name='getupdateequipmentpage'),
    path('updatequipment/', views.UpdateEquipment, name='updatequipment'),
    path('getaddequipmentpage/', views.GetEqueipmentPage ,name='getaddequipmentpage'),
    path('deleteequiment/<str:equipment_id>/', views.DeleteEquipment, name='deleteequiment'),

    path('getaddattendancepage/', views.GetAddAttentancePage, name='getaddattendancepage'),
    path('showallattedace/', views.ShowAllAttendance, name='showallattedace'),
    path('getupdateattendancepage/<str:attendance_id>/', views.GetUpdateAttendancePage, name='getupdateattendancepage'),
    path('deleteattendance/<str:attendance_id>/', views.DeleteAttendance, name='deleteattendance'),
    path('updateattendance/', views.UpdateAttendance, name='updateattendance'),
    path('addattendance/', views.AddAttendance, name='addattendance'),

    path('getaddpaymentpage/', views.GetAddPaymentPage, name='getaddpaymentpage'),
    path('showallpayments/', views.ShowAllPayment, name='showallpayments'),
    path('getupdatepaymentpage/<str:payment_id>/', views.GetUpdatePaymentPage, name='getupdatepaymentpage'),
    path('deletepayment/<str:payment_id>/', views.DeletePayment, name='deletepayment'),
    path('updatepayment/', views.UpdatePayment, name='updatepayment'),
    path('addpayment/', views.AddPayment, name='addpayment'),

    path('getaddfeedbackpage/', views.GetAddFeedbackPage, name='getaddfeedbackpage'),
    path('showallfeedbacks/', views.ShowAllFeedback, name='showallfeedbacks'),
    path('getupdatefeedbackpage/<str:feedback_id>/', views.GetUpdateFeedbackPage, name='getupdatefeedbackpage'),
    path('deletefeedback/<str:feedback_id>/', views.DeleteFeedback, name='deletefeedback'),
    path('updatefeedback/', views.UpdateFeedback, name='updatefeedback'),
    path('addfeedback/', views.AddFeedback, name='addfeedback'),

    path('showallmembers/', views.ShowAllMembers, name='showallmembers'),
    path('getaddmemberpage/', views.GetAddMemberPage, name='getaddmemberpage'),
    path('getupdatememberpage/<str:username>/', views.GetUpdateMemberPage, name='getupdatememberpage'),
    path('deletemember/<str:username>/', views.DeleteMember, name='deletemember'),
    path('updatemember/', views.UpdateMember, name='updatemember'),
]