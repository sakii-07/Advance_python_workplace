from django.shortcuts import render, redirect
from .models import UserInfo, Product
from django.contrib.auth import logout
# Create your views here.
def GetSigninPage(request):
    return render(request, 'signin.html')

def Signin(request):
    username = request.GET['username']
    mobile = request.GET['mobile']
    password = request.GET['password']

    UserInfo.objects.create(
        username = username,
        mobile = mobile,
        password = password
    )
    return render(request, 'login.html',{'suc_msg':"Sign in successfully ..."})

def GetLoginPage(request):
    return render(request, 'login.html')

def Login(request):
    username = request.GET['username']
    password = request.GET['password']

    if username:
        user_db = UserInfo.objects.get(username = username)

        if username == user_db.username and password == user_db.password:
            request.session['username'] = username
            return redirect('gethomepage')
        else:
            return render(request, 'login.html', {'msg':'Invalid Username and password ...'})
        
def GetNavbar(request):
    return render(request, 'base.html')

def GetHomePage(request):
    return render(request, 'home.html')

def Logout(request):
    logout(request)
    return redirect('getloginpage')

def GetProductFormPage(request):
    return render(request,'products_form.html')

def ShowProductsPage(request):
    product_db = Product.objects.all()
    if product_db:
        return render(request, 'show_products.html',{'product_db':product_db})

def AddProduct(request):
    product_name = request.GET['product_name']
    category = request.GET['category']
    brand = request.GET['brand']
    price = request.GET['price']
    stock = request.GET['stock']
    description = request.GET['description']
    image = request.FILES['image']
    manufacturing_date = request.GET['manufacturing_date']
    expiry_date = request.GET['expiry_date']

    Product.objects.create(
        product_name = product_name,
        category = category,
        brand = brand,
        price = price,
        stock = stock,
        description = description,
        image = image,
        manufacturing_date = manufacturing_date,
        expiry_date = expiry_date
    )
    return render(request, 'show_products.html')

def UpdateProduct(request):
   products_db =  Product.objects.filter()

   products_db.update(
       product_name = request.GET['product_name'],
        category = request.GET['category'],
        brand = request.GET['brand'],
        price = request.GET['price'],
        stock = request.GET['stock'],
        description = request.GET['description'],
        image = request.GET['image'],
        manufacturing_date = request.GET['manufacturing_date'],
        expiry_date = request.GET['expiry_date']
    )
   return redirect('getshowallproductpage')

def GetUpdateProductPage(request,product_name):
    if product_name:
        product_db = Product.objects.get(product_name = product_name)
        return render(request, 'update_products.html',{'product_db':product_db})
    else:
        return render(request, 'update_products.html',{'msg':'Wrong Product Name'})


def DeleteProduct(request, product_name):
    if product_name:
        Product.objects.get(product_name=product_name).delete()
        return redirect('getshowallproductpage')
    else:
        return render(request, 'update_products.html',{'msg':'Wrong Product Name'})

def GetUserDetailsPage(request):
    username = request.session.get('username')
    user = UserInfo.objects.get(username = username)
    return render(request, 'user_details.html',{'user':user})

def UserDetails(request):
    username = request.session.get('username')
    if username:
        user = UserInfo.objects.get(username = username)
        return render(request, 'user_details.html',{'user':user})
    else:
        return render(request, 'home.html')
    
def GetUpdateUserDetailsPage(request,username):

    if username:
        user = UserInfo.objects.get(username = username)
        return render(request, 'update_userinfo.html', {'user':user})
    else:
        return render(request, 'update_userinfo.html',{'msg':'Invalid Username'})

def UpdateUserDetails(request):
    username = request.GET['username']
    if username:
        user_details = UserInfo.objects.filter(username = username)
        user_details.update(
                mobile = request.GET['mobile'],
                password = request.GET['password']
            )
        return redirect('getuserdetailspage')
    else:
        return render(request, 'update_userinfo.html',{'msg':'Invalid Username'})

