from django.shortcuts import render,redirect
from .models import Question, UserInfo, Result
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
        return redirect('gethomepage')
    else:
        return render(request, 'User/signup.html',{'msg':'Invalid username or password'})

def GetLoginPage(request):
    return render(request, 'User/login.html')

def Login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = UserInfo.objects.get(username=username)

            if password == user.password:
                request.session["username"] = username
                request.session["answer"] = {}
                request.session["score"] = 0
                request.session["qno"] = 0

                return redirect('gethomepage')

            else:
                return render(request, "User/login.html", {"msg": "Invalid Password"})

        except UserInfo.DoesNotExist:
            return render(request, "User/login.html", {"msg": "Invalid Username"})

    return render(request, "User/login.html")
        
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

def GetUpdateUserPage(request,username):
    if username:
        user = UserInfo.objects.get(username = username)
        return render(request, 'User/update_user_1.html',{'user':user})
    return render(request, 'User/show_all_user.html')

def UpdateUser(request):
    username = request.POST['username']
    if username:
        user = UserInfo.objects.filter(username = username)
        user.update(
            password = request.POST['password'],
            mobile = request.POST['mobile']
            )
        return redirect('getshowallpage')
    return render(request, 'User/show_all_user.html')

def GetUserModulePage(request):
    return render(request, 'User/user_module.html')

def GetShowAllUserPage(request):
    user_db = UserInfo.objects.all()
    return render(request, 'User/show_all_user.html',{'user_db':user_db})

def GetInstructionPage(request):
    return render(request,'Test/instruction.html')

def GetSubjestPage(request):
    subjects = Question.objects.values_list("subject", flat=True).distinct()
    return render(request, "Test/select_subject.html", {"subjects": subjects})
    
def StartTest(request):
    subject = request.GET["subject"]
    request.session['subject'] = subject

    question = Question.objects.filter(subject=subject).values('qno',
            'qtext',
            'op1',
            'op2',
            'op3',
            'op4',
            'corr_answer',   
            'subject')

    allquestions = list(question)

    if not allquestions:
        return render(request, "Test/select_subject.html",{"msg": "No Questions Available"})
    
    request.session['allquestions'] = allquestions

    return render(request, "Test/question_page.html", {"subject": subject,"question": allquestions[0]})

def NextQuestion(request):
    allquestions = request.session['allquestions']
    questionindex = request.session['qno']

    if 'op' in request.GET:
        allanswer = request.session['answer']
        allanswer[request.GET['qno']] = [request.GET['qno'], request.GET['qtext'],request.GET['op'],request.GET['answer']]
    try:
        if questionindex < len(allquestions)-1:
            request.session['qno'] += 1
            question = allquestions[request.session['qno']]
            return render(request,'Test/question_page.html',{'question':question})
        else:
            return render(request, 'Test/question_page.html', {
                'question': allquestions[-1],
                'msg': 'This is the last question.'
            })
    except Exception as e:
        return render(request,'Test/question_page.html',{'msg':'Go to previous question ','question':allquestions[-1]})

def PreviousQuestion(request):
    allquestions = request.session['allquestions']
    questionindex = request.session['qno']

    allanswer = request.session.get('answer', {})

    if 'op' in request.GET:
        # allanswer = request.session['answer']
        allanswer[request.GET['qno']] = [request.GET['qno'], request.GET['qtext'], request.GET['op'],request.GET['answer']]
    request.session['answer'] = allanswer

    try:
        if questionindex > 0:
            request.session['qno'] -= 1
            question = allquestions[request.session['qno']]
            return render(request, 'Test/question_page.html',{'question':question})
        else:
            return render(request, 'Test/question_page.html', {
                'question': allquestions[0],
                'msg': 'This is the first question.'
            })
    except Exception as e:
        return render(request, 'Test/question_page.html',{'msg':'Go to previous question','question':allquestions[0]})

def EndTest(request):
    allanswer = request.session.get('answer', {})
    if 'op' in request.GET:
        # allanswer = request.session['answer']
        allanswer[request.GET['qno']] = [request.GET['qno'], request.GET['qtext'], request.GET['op'],request.GET['answer']]
    request.session['answer'] = allanswer
    response = list(allanswer.values())

    request.session['score'] = 0
    
    for res in response:
        if res[2] == res[3]:
            request.session['score'] += 1

    finalscore = request.session['score']
    username = request.session['username']

    user = UserInfo.objects.get(username = username)

    Result.objects.create(
        username = user,
        subject = request.GET['subject'],
        score = finalscore
    )
    return render(request,'Result/Score.html',{'response':response,'finalscore':finalscore})

def ShowAllresult(request):
    rdb = Result.objects.all()
    return render(request,'Result/showallresult.html',{'rdb':rdb})

def GetDeleteUserPage(request):
    return render(request, 'User/delete_user.html')

def Deleteuser(request,username):
    UserInfo.objects.get(username = username).delete()
    return redirect('getshowallpage')

def DeleteUser1(request):
    if request.method == "POST":
        username = request.POST.get("username")
        try:
            user = UserInfo.objects.get(username=username)
            user.delete()
            msg = "User Deleted Successfully."
        except UserInfo.DoesNotExist:
            msg = "Invalid Username."

        return render(request, "User/delete_user.html", {"msg": msg})
    return render(request, "User/delete_user.html")