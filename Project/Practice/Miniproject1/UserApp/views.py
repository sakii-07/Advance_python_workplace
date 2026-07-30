from django.shortcuts import render
from .models import CustomerInfo

# Create your views here.
def GetCheckCustomerPage(request):
    return render(request, 'checkcustomer.html')

def CheckCustomer(request):
    try:
        custid = request.GET['cid']

        customer = CustomerInfo.objects.get(cid = custid)

        if customer.cid == int(custid):
            return render(request, 'checkcustomer.html',{'msg':'Customer exist with salary : ', 'customer':customer})
        else:
            return render(request, 'checkcustomer.html',{'msg':'Customer not exist'})
    except Exception as e:
        return render(request, 'checkcustomer.html',{'msg':'Customer not exist'})

def AddCustomer(request):
    custid = request.GET['cid']
    cname = request.GET['name']
    csalary = request.GET['salary']

    CustomerInfo.objects.create(
        cid = custid,
        name = cname,
        salary = csalary
    )