from django.shortcuts import render, redirect
from .models import StudentIfo, SigninInfo
from django.contrib.auth import logout

# Create your views here.

def GetRegistrationPage(request):
    return render(request, 'registration.html')

def Register(request):
    fname = request.GET['fname']
    lname = request.GET['lname']
    email = request.GET['email']
    mobile = request.GET['mobile']
    dob = request.GET['dob']
    gender = request.GET['gender']
    address = request.GET['address']
    course = request.GET['course']
    semester = request.GET['semester']
    username = request.GET['username']
    password = request.GET['password']

    StudentIfo.objects.create(
        fname = fname,
        lname = lname,
        email = email,
        mobile = mobile,
        dob = dob,
        gender = gender,
        address = address,
        course = course,
        semester = semester,
        username = username,
        password = password
    )

    return render(request, 'registration.html', {'msg':'Student Registered Successfully ...'})

def Navbar(request):
    return render(request, 'base.html')


def ShowAllStudents(request):
    students = StudentIfo.objects.all()
    return render(request, 'showallstudents.html', {'students':students})

def GetUpdatePage(request):
    return render(request, 'update.html')

def ShowStudentForUpdate(request):
    username = request.GET['username']
    students = StudentIfo.objects.get(username = username)
    if students:
        return render(request, "update.html", {'students':students})
    else:
        return render(request,'update.html',{"msg":'Invalid Username'})
    
def UpdateForShowAll(request, username):
    students = StudentIfo.objects.get(username = username)
    if students:
        return render(request, "update.html", {'students':students})
    else:
        return render(request,'update.html',{"msg":'Invalid Username'})
    
def Update(request):
    username = request.GET['username']

    if username:
        student_db = StudentIfo.objects.filter(username = username)
        student_db.update(
            fname = request.GET['fname'],
            lname = request.GET['lname'],
            email = request.GET['email'],
            mobile = request.GET['mobile'],
            dob = request.GET['dob'],
            gender = request.GET['gender'],
            address = request.GET['address'],
            course = request.GET['course'],
            semester = request.GET['semester'],
            password = request.GET['password'],
        )
        return redirect('showallstudents')
    else:
        return render(request, 'showallstudents.html', {'msg':'Invalid Username'})

def GetDeletePage(request):
    return render(request, 'delete.html')

def DeleteStudentForShowall(request, username):
    StudentIfo.objects.get(username = username).delete()
    return redirect('showallstudents')

def Delete(request):
    username = request.GET['username']
    if username:
        StudentIfo.objects.get(username = username).delete()
        return redirect('showallstudents')
    else:
        return render(request, 'delete.html',{'mgs':'Invalid Username'})
    
def GetLoginPage(request):
    return render(request, 'login.html')

def LoginStudent(request):
    username = request.GET['username']
    password = request.GET['password']

    student_db = SigninInfo.objects.get(username = username)


    if student_db.username == username.strip() and student_db.password == password:
        request.session['username'] = username
        return redirect('showallstudents')
    else:
        return render(request,'login.html',{'msg':'Invalid Username and Password..'})
    
def Logout(request):
    logout(request)
    return render(request, 'login.html',{'msg':'Logout successfully..'})

def GetSigninPage(request):
    return render(request, 'signin.html')

def SignIn(request):
    username = request.GET['username']
    password = request.GET['password']

    if username:
        SigninInfo.objects.create(
            username = username,
            password = password
        )
        return render(request,"login.html")
    else:
        return render(request, 'signin.html',{'msg':'username already exist..'})