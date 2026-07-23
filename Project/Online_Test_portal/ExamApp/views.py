from django.shortcuts import render,redirect
from .models import Question, UserInfo
from django.contrib.auth import logout

# Create your views here.
def GetAddQuestionPage(request):
    return render(request, 'Questions/addquestion.html')

def AddQuestion(request):
    if request.method == 'POST':
        qtext = request.POST['qtext']
        op1 = request.POST['op1']
        op2 = request.POST['op2']
        op3 = request.POST['op3']
        op4 = request.POST['op4']
        corr_answer = request.POST['corr_answer']
        subject = request.POST['subject']

        Question.objects.create(
            qtext = qtext,
            op1 = op1,
            op2 = op2,
            op3 = op3,
            op4 = op4,
            corr_answer = corr_answer,
            subject = subject
        )
        return redirect('showallquestion')
    else:
        return render(request, 'Questions/addquestion.html')


def ShowAllQuestions(request):
    question_db = Question.objects.all()
    return render(request, 'Questions/showallquestion.html', {'question_db':question_db})

def GetUpdateQuestionPage(request,qno):
    question = Question.objects.get(qno = qno)
    return render(request, 'Questions/update_question.html',{'question':question})

def UpdateQuestion(request):
    if request.method == 'POST':
        qno = request.POST['qno']
        question_db = Question.objects.filter(qno = qno)
        question_db.update(
            qtext = request.POST['qtext'],
            op1 = request.POST['op1'],
            op2 = request.POST['op2'],
            op3 = request.POST['op3'],
            op4 = request.POST['op4'],
            corr_answer = request.POST['corr_answer'],
            subject = request.POST['subject']
        )
        return redirect('showallquestion')
    else:
        return render(request,'Questions/update_question.html',{'msg':'Invalid Question Number'})
    
def DeleteQuestion(request,qno):
    Question.objects.get(qno = qno).delete()
    return redirect('showallquestion')

def GetQuestionNavbarPage(request):
    return render(request, 'Questions/question_navbar.html')

def Logout(request):
    logout(request)
    return render(request,'User/login.html')

def GetSignupPage(request):
    return render(request, 'User/signup.html')

def Signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        mobile = request.POST['mobile']

        UserInfo.objects.create(
            username = username,
            password = password,
            mobile = mobile
        )
        return redirect('showallquestion')
    else:
        return render(request, 'User/signup.html',{'msg':'Invalid username or password'})

def GetLoginPage(request):
    return render(request, 'User/login.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = UserInfo.objects.get(username = username)

        if user.username == username and password == user.password:
            request.session['username'] = username
            return redirect('gethomepage')
        else:
            return render(request,'User/login.html',{'msg':'invalid username'})
        
def GetHomePage(request):
    return render(request, 'Home/home.html')

def GetMyprofilePage(request):
    username = request.session.get('username')
    if username:
        user = UserInfo.objects.get(username = username)
        return render(request, 'User/myprofile.html',{'user':user})
    return render(request, 'User/login.html')

def GetUpdateProfilePage(request):
    username = request.session.get('username')
    if username:
        user = UserInfo.objects.get(username = username)
        return render(request, 'User/update_user.html',{'user':user})
    return render(request, 'User/myprofile.html')

def UpdateProfile(request):
    username = request.POST['username']
    if username:
        user = UserInfo.objects.filter(username = username)
        user.update(
            password = request.POST['password'],
            mobile = request.POST['mobile']
        )
        return redirect('getmyprofilepage')
    return render(request, 'User/myprofile.html')

def GetUserModulePage(request):
    return render(request, 'User/user_module.html')

def GetShowAllUserPage(request):
    user_db = UserInfo.objects.all()
    return render(request, 'User/show_all_user.html',{'user_db':user_db})

