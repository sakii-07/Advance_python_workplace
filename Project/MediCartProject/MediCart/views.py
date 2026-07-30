from django.shortcuts import render,redirect
from .models import UserInfo,Medicine
from django.contrib.auth import logout

# Create your views here.
def GetSignUpPage(request):
    return render(request, 'signup.html', {'msg':'User Signed Up Successfully!!'})

def SignUp(request):
    username=request.GET['username']
    mobile=request.GET['mobile']
    password=request.GET['password']

    UserInfo.objects.create(
        username=username,
        mobile=mobile,
        password=password
    )

    return render(request,'login.html')

def GetLoginPage(request):
    return render(request, 'login.html', {'msg':'User Logged In Successfully!!!'})

def Login(request):
    username = request.GET['username']
    password = request.GET['password']

    if username:
        user_db = UserInfo.objects.get(username = username)

        if username == user_db.username and password == user_db.password:
            request.session['username'] = username
            return redirect('homepage')
        else:
            return render(request, 'login.html', {'msg':'Invalid Username and password ...'})
    
def GetNavbar(request):
    return render(request, 'base.html')

def GetHomePage(request):
    return render(request, 'home.html')

def GetAddMedicinePage(request):
    return render(request, 'add.html')

def AddMedicine(request):
      medicine_name=request.GET['medicine_name']
      company=request.GET['company']
      price=request.GET['price']
      quantity=request.GET['quantity']
      mfg_date=request.GET['mfg_date']
      exp_date=request.GET['exp_date']
      description=request.GET['description']

      Medicine.objects.create(
          medicine_name=medicine_name,
          company=company,
          price=price,
          quantity=quantity,
          mfg_date=mfg_date,
          exp_date=exp_date,
          description=description
      )

      return redirect('viewallmed')

def GetViewMedicinePage(request):
    medicine = Medicine.objects.all()

    return render(request, 'viewmed.html', {'medicine': medicine})


def ViewMedPage(request):
    medicine = Medicine.objects.all()
    return render(request, 'viewmed.html',{'medicine':medicine})

def GetUpdateMedPage(request,id):
    if id:
        medicine_db = Medicine.objects.get(id=id)
        return render(request, 'update_med.html',{'medicine':medicine_db})
    else:
        return render(request, 'update_med.html',{'msg':'Wrong Medicine Name'})


def UpdateMed(request):
   medicine_db=Medicine.objects.filter(id=request.GET['id'])

   medicine_db.update(
        medicine_name = request.GET['medicine_name'],
        company = request.GET['company'],
        price = request.GET['price'],
        quantity = request.GET['quantity'],
        mfg_date = request.GET['mfg_date'],
        exp_date = request.GET['exp_date'],
        description=request.GET['description']
    )

   
   return redirect('viewallmed')

def DeleteMedicine(request,id):
    Medicine.objects.get(id=id).delete()
    return redirect('viewmed')

def GetCategoriesPage(request):
    return render(request, 'categories.html')

def Logout(request):
    logout(request)
    return redirect('getloginpage')


def GethealthcaePage(request):
    return render(request, 'healthcare.html')


def GetaboutPage(request):
    return render(request, 'about.html')
    