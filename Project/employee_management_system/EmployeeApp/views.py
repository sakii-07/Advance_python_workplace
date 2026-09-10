from django.shortcuts import render,redirect
from .models import Employee
from .modelform import EmployeeModelForm
from django.db.models import Avg, Count

# Create your views here.

def Dashboard(request):

    total_employees = Employee.objects.count()

    total_departments = Employee.objects.values(
        "department"
    ).distinct().count()

    average_salary = Employee.objects.aggregate(
        Avg("salary")
    )["salary__avg"]

    context = {
        "total_employees": total_employees,
        "total_departments": total_departments,
        "average_salary": round(average_salary, 2)
        if average_salary else 0,
        "new_employees": 0,
    }

    return render(
        request,
        "dashboard.htm",
        context
    )

def AddEmployee(request):
    if request.method == "POST":
        modelform = EmployeeModelForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return render(request,"addemployee.htm",{'msg':'Employee Added Successfully...'})
        return render(request,"addemployee.htm",{'errmsg':'Unable to Add Employee...'})
    else:
        modelform = EmployeeModelForm()
    return render(request,"addemployee.htm",{'form':modelform})

def ShowEmployees(request):
    employees = Employee.objects.all()
    return render(request,"showemployee.htm",{"employees":employees})

def DeleteEmployee(request,empId):
    Employee.objects.get(empId = empId).delete()
    return redirect("showemployee")

def GetUpdateEmployeePage(request,empId):
    employee = Employee.objects.get(empId = empId)
    return render(request,"updateemployee.htm",{'employee':employee})

def UpdateEmployee(request, empId):
    employee = Employee.objects.get(empId = empId)
    if request.method == "POST":
        modelform = EmployeeModelForm(request.POST, instance=employee)
        if modelform.is_valid():
            modelform.save()
            return redirect("showemployee")
        return render(request,"updateemployee.htm",{'errmsg':'Unable to Update Employee...'})
    else:
        modelform = EmployeeModelForm(instance=employee)
    return render(request,"updateemployee.htm",{'form':modelform,"employee": employee})