from django.urls import path
from . import views

urlpatterns = [
    path('getaddquestionpage/', views.GetAddQuestionPage, name='getaddquestionpage'),
    path('addquestion/', views.AddQuestion, name='addquestion'),

    path('showallquestion/', views.ShowAllQuestions, name='showallquestion'),

    path('getupdatequestionpage/<str:qno>/', views.GetUpdateQuestionPage, name='getupdatequestionpage'),
    path('updatequestion/', views.UpdateQuestion, name='updatequestion'),

    path('deletequestion/<str:qno>/', views.DeleteQuestion, name='deletequestion'),

    path('getquestionnavbarpage/', views.GetQuestionNavbarPage, name='getquestionnavbarpage'),

    path('', views.GetSignupPage, name='getsignuppage'),
    path('signup/', views.Signup, name='signup'),

    path('getloginpage/', views.GetLoginPage, name='getloginpage'),
    path('login/', views.Login, name='login'),

    path('logout/', views.Logout, name='logout'),

    path('gethomepage/', views.GetHomePage, name='gethomepage'),
    path('getmyprofilepage/', views.GetMyprofilePage, name='getmyprofilepage'),
    path('getupdateprofilepage/', views.GetUpdateProfilePage, name='getupdateprofilepage'),
    path('updateprofile/', views.UpdateProfile, name='updateprofile'),

    path('updateuser/', views.UpdateUser, name='updateuser'),
    path('getupdateuserpage/<str:username>/', views.GetUpdateUserPage, name='getupdateuserpage'),

    path('getusermodulepage/', views.GetUserModulePage, name='getusermodulepage'),
    path('getshowallpage/', views.GetShowAllUserPage, name='getshowallpage'),

    path('getinstructionpage/', views.GetInstructionPage, name='getinstructionpage'),
    path('starttest/', views.StartTest, name='starttest'),
    path('getsubjectpage/', views.GetSubjestPage, name='getsubjectpage'),

    path('nextquestion/', views.NextQuestion, name='nextquestion'),
    path('previousquestion/', views.PreviousQuestion, name='previousquestion'),
    path('endtest/', views.EndTest, name='endtest'),
    path('showallresult/', views.ShowAllresult, name='showallresult'),
    path('getdeleteuserpage/', views.GetDeleteUserPage, name='getdeleteuserpage'),

    path('deleteuser/<str:username>/', views.Deleteuser, name='deleteuser')

]
