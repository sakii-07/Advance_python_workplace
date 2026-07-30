from django.shortcuts import render
from .models import CustomerInfo
# Create your views here.

def GetCheckCustomerPage(request):
    return render(request, 'checkcustomer.html')

def CheckCustomer(request):
    try:
        cid = request.GET['cid']

        customer = CustomerInfo.objects.get(cid = cid)

        if customer.cid == int(cid):
            return render(request, 'checkcustomer.html', {'msg':'Customer exist with : ','customer':customer})
        else:
            return render(request, 'checkcustomer.html', {'msg':'Customer not exist'})
    except Exception as e:
        return render(request, 'checkcustomer.html', {'msg':'Customer not exist'})