from django.shortcuts import render, redirect
from .models import UserInfo, Attendance, Feedback, Trainer, Equipment,Payment
from django.contrib.auth import logout

# Create your views here.
def GetDashboardPage(request):
    return render(request, 'dashboard.html')

def GetRegisterPage(request):
    return render(request, 'register.html')

def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']

        UserInfo.objects.create(
            username = username,
            email = email,
            password = password,
            mobile = mobile
        )
        return render(request,'dashboard.html')
    else:
        return render(request, 'register.html',{'msg':'Invalid username or password'})

def GetLoginPage(request):
    return render(request, 'login.html')

from django.shortcuts import render, redirect
from .models import UserInfo

def Login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = UserInfo.objects.get(
                username=username,
                password=password
            )
            if user :
                request.session["username"] = user.username
                return redirect("getdashboardpage")

        except UserInfo.DoesNotExist:

            return render(request, "login.html", {
                "msg": "Invalid Username or Password"
            })

    return render(request, "login.html")
        

def GetMyprofilePage(request):
    username = request.session.get('username')
    if username:
        user = UserInfo.objects.get(username = username)
        return render(request, 'myprofile.html',{'user':user})
    return render(request, 'login.html')

def GetUpdateProfilePage(request):
    username = request.session.get('username')
    if username:
        user = UserInfo.objects.get(username = username)
        return render(request, 'update_user.html',{'user':user})
    return render(request, 'myprofile.html')

def UpdateProfile(request):
    username = request.POST['username']
    if username:
        user = UserInfo.objects.filter(username = username)
        user.update(
            password = request.POST['password'],
            email = request.POST['email'],
            mobile = request.POST['mobile']
        )
        return redirect('getmyprofilepage')
    return render(request, 'myprofile.html')

def Logout(request):
    logout(request)
    return redirect('getloginpage')


def GetAddTrainerPage(request):
    return render(request,'trainer.html')

def ShowAllTrainers(request):
    trainers = Trainer.objects.all()
    return render(request,'show_trainers.html',{'trainers':trainers})

def AddTrainer(request):
    if request.method == "POST":
        trainer_name = request.POST['trainer_name']
        specialization = request.POST['specialization']
        experience = request.POST['experience']
        mobile = request.POST['mobile']
        email = request.POST['email']
        salary = request.POST['salary']
        joining_date = request.POST['joining_date']

        Trainer.objects.create(
            trainer_name = trainer_name,
            specialization = specialization,
            experience = experience,
            mobile = mobile,
            email = email,
            salary = salary,
            joining_date = joining_date
        )
        return redirect('showalltrainers')

def GetUpdateTrainerPage(request,trainer_id):
    if trainer_id:
        trainer = Trainer.objects.get(trainer_id=trainer_id)
        return render(request, 'update_trainer.html',{'trainer':trainer}) 
    else:
        return redirect('showalltrainers')

def UpdateTrainer(request):
    trainer_id = request.POST['trainer_id']
    if trainer_id:
        triner = UserInfo.objects.filter(trainer_id = trainer_id)
        triner.update(
            specialization = request.POST['specialization'],
            experience = request.POST['experience'],
            mobile = request.POST['mobile'],
            email = request.POST['email'],
            salary = request.POST['salary'],
            joining_date = request.POST['joining_date']
        )
        return redirect('showalltrainers')
    return redirect('showalltrainers')

def ShowAllEquipmnts(request):
    equipments = Equipment.objects.all()
    return render(request,'show_equipment.html',{'equipments':equipments})

def GetEqueipmentPage(request):
    return render(request,'equipment.html')

def AddEquipment(request):
    if request.method == "POST":
        equipment_name = request.POST['equipment_name']
        brand = request.POST['brand']
        quantity = request.POST['quantity']
        purchase_date = request.POST['purchase_date']
        status = request.POST['status']
        Equipment.objects.create(
            equipment_name = equipment_name,
            brand = brand,
            quantity = quantity,
            purchase_date = purchase_date,
            status = status
        )
        return redirect('showallequipmnts')

def GetUpdateEquipmentPage(request,equipment_id):
    if equipment_id:
        equipment = Equipment.objects.get(equipment_id=equipment_id)
        return render(request, 'update_equipment.html',{'equipment':equipment}) 
    else:
        return redirect('showallequipmnts')

def UpdateEquipment(request):
    equipment_id = request.POST['equipment_id']
    if equipment_id:
        equipments = UserInfo.objects.filter(equipment_id = equipment_id)
        equipments.update(
            equipment_name = request.POST['equipment_name'],
            brand = request.POST['brand'],
            quantity = request.POST['quantity'],
            purchase_date = request.POST['purchase_date'],
            status = request.POST['status']
        )
        return redirect('showallequipmnts')
    return redirect('showallequipmnts')

def DeleteEquipment(request,equipment_id):
    if equipment_id:
        Equipment.objects.get(equipment_id = equipment_id).delete()
        return redirect('showallequipmnts')

def ShowAllAttendance(request):
    attendances = Attendance.objects.all()
    return render(request,'show_attendance.html',{'attendances':attendances})

def GetAddAttentancePage(request):
    # users = UserInfo.objects.values_list('username', flat=True).distinct
    users = UserInfo.objects.all()
    return render(request,'attendance.html',{'users':users})

def AddAttendance(request):
    username = request.POST['username']
    user = UserInfo.objects.get(username=username)
    if user:
        attendance_date = request.POST['attendance_date']
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        status = request.POST['status']

        Attendance.objects.create(
            username = user,
            attendance_date = attendance_date,
            check_in = check_in,
            check_out = check_out,
            status = status
        )
        return redirect('showallattedace')
    else:
        return render(request,'attendance.html',{'msg':'Invalid username'})

def GetUpdateAttendancePage(request,attendance_id):
    if attendance_id:
        users = UserInfo.objects.all()
        attendance = Attendance.objects.get(attendance_id=attendance_id)
        return render(request, 'update_attendance.html',{'attendance':attendance,'users':users}) 
    else:
        return redirect('showallattedace')

def UpdateAttendance(request):
    attendance_id = request.POST['attendance_id']
    if attendance_id:
        attendance = Attendance.objects.filter(attendance_id = attendance_id)
        attendance.update(
                username = request.POST['username'],
                attendance_date = request.POST['attendance_date'],
                check_in = request.POST['check_in'],
                check_out = request.POST['check_out'],
                status = request.POST['status']
        )
        return redirect('showallattedace')
    return redirect('showallattedace')

def DeleteAttendance(request,attendance_id):
    Attendance.objects.get(attendance_id = attendance_id).delete()
    return redirect('showallattedace')


def ShowAllPayment(request):
    payments = Payment.objects.all()
    return render(request,'show_payment.html',{'payments':payments})

def GetAddPaymentPage(request):
    # users = UserInfo.objects.values_list('username', flat=True).distinct
    users = UserInfo.objects.all()
    return render(request,'payment.html',{'users':users})

def AddPayment(request):
    username = request.POST['username']
    user = UserInfo.objects.get(username=username)
    if user:
        amount = request.POST['amount']
        payment_mode = request.POST['payment_mode']
        payment_date = request.POST['payment_date']
        payment_status = request.POST['payment_status']

        Payment.objects.create(
            username = user,
            amount = amount,
            payment_mode = payment_mode,
            payment_date = payment_date,
            payment_status = payment_status,
        )
        return redirect('showallpayments')
    else:
        return render(request,'payment.html',{'msg':'Invalid username'})

def GetUpdatePaymentPage(request,payment_id):
    if payment_id:
        users = UserInfo.objects.all()
        payment = Payment.objects.get(payment_id=payment_id)
        return render(request, 'update_payment.html',{'payment':payment,'users':users}) 
    else:
        return redirect('showallpayments')

def UpdatePayment(request):
    payment_id = request.POST['payment_id']
    if payment_id:
        username = request.POST['username']
        user = UserInfo.objects.get(username = username)
        payment = Payment.objects.filter(payment_id = payment_id)
        payment.update(
            username = user,
            amount = request.POST['amount'],
            payment_mode = request.POST['payment_mode'],
            payment_date = request.POST['payment_date'],
            payment_status = request.POST['payment_status']    
        )
        return redirect('showallpayments')
    return redirect('showallpayments')

def DeletePayment(request,payment_id):
    Payment.objects.get(payment_id = payment_id).delete()
    return redirect('showallpayments')


def ShowAllFeedback(request):
    Feedbacks = Feedback.objects.all()
    return render(request,'show_feedback.html',{'Feedbacks':Feedbacks})

def GetAddFeedbackPage(request):
    # users = UserInfo.objects.values_list('username', flat=True).distinct
    users = UserInfo.objects.all()
    return render(request,'feedback.html',{'users':users})

def AddFeedback(request):
    username = request.POST['username']
    user = UserInfo.objects.get(username=username)
    if user:
        rating = request.POST['rating']
        review = request.POST['review']
        Feedback.objects.create(
            username = user,
            rating = rating,
            review = review
        )
        return redirect('showallfeedbacks')
    else:
        return render(request,'feedback.html',{'msg':'Invalid username'})

def GetUpdateFeedbackPage(request,feedback_id):
    if feedback_id:
        users = UserInfo.objects.all()
        feedback = Feedback.objects.get(feedback_id=feedback_id)
        return render(request, 'update_feedback.html',{'feedback':feedback,'users':users}) 
    else:
        return redirect('showallfeedbacks')

def UpdateFeedback(request):
    feedback_id = request.POST['feedback_id']
    if feedback_id:
        username = request.POST['username']
        user = UserInfo.objects.get(username = username)
        feedback = Feedback.objects.filter(feedback_id = feedback_id)
        feedback.update(
            username = user, 
            rating = request.POST['rating'],
            review = request.POST['review']
        )
        return redirect('showallfeedbacks')
    return redirect('showallfeedbacks')

def DeleteFeedback(request,feedback_id):
    Feedback.objects.get(feedback_id = feedback_id).delete()
    return redirect('showallfeedbacks')

def ShowAllMembers(request):
    members = UserInfo.objects.all()
    return render(request,'show_members.html',{'members':members})

def GetAddMemberPage(request):
    return render(request, 'add_member.html')

def GetUpdateMemberPage(request,username):
    if username:
        member = UserInfo.objects.get(username = username)
        return render(request, 'update_member.html',{'member':member}) 
    else:
        return redirect('showallmembers')

def UpdateMember(request):
    username = request.POST['username']
    if username:
        user = UserInfo.objects.filter(username = username)
        user.update(
            email = request.POST['email'],
            password = request.POST['password'],
            mobile = request.POST['mobile']
        )
        return redirect('showallmembers')
    return redirect('showallmembers')

def DeleteMember(request,username):
    UserInfo.objects.get(username = username).delete()
    return redirect('showallmembers')