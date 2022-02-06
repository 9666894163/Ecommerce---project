from contextvars import Context
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from numpy import False_, product
from .models import *
from .forms import *


# Create your views here.
from django.shortcuts import render
from .models import *

# Create your views here.


@login_required(login_url='login')
def Home(request):

    prods = Products.objects.all()
    context = {
        'products': prods
    }
    return render(request,'home.html',context)

def category(request):

    cat = Category.objects.all()    
    context = {
        'category': cat
    }
    return render(request,'home.html',context)

def View_options(request,id):

    product_object = Products.objects.get(pk = id)

    context  = {
        'search': product_object
    }

    return render(request,'search.html',context) 

def Register_form(request):
    # if request.method =='POST':
    #     first_name = request.POST['First Name']
    #     last_name = request.POST['Last Name']
    #     phone = request.POST.get['Phone number']
    #     email = request.POST['Email']
    #     password = request.POST['Password']
    #     print(first_name,last_name,phone,email,password)
    #     customer = Customer( first_name = first_name,last_name= last_name,phone = phone,email = email,password=password)
    #     customer.save()
    #     return HttpResponse(request.POST('email'))

    #return render(request,'register.html')    
    if request.method == 'POST':
        form = Registration_user(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = Registration_user()        
    return render(request,'register.html',{'form':form})

def Login(request):
    if request.method == 'POST':
        U = request.POST['username']
        P = request.POST['password']
        obj = authenticate(request,username =U,password = P)
        if obj is not None:
            login(request,obj)
            return redirect('home')
        else:
            messages.error(request,'Invalid crediantials')
            return render(request,'login.html')
    else:
        return render(request,'login.html') 


@login_required(login_url='login')
# def signout(request):
#     if request.user.is_authenticated:
#         logout(request)
#         return redirect('log')
#     else:
#         return render(request,'home.html')    

    # logout(request)
    # messages.info(request,'You have sussefully logout')
    # return redirect('home.html')


def cart(request,name):
    print(name)
    print('cart.called')
    if request.method =='POST':
        valid_prd = Products.objects.filter(name = name)
        if valid_prd is not None:
             ord = Orders()
             ord.user = request.user
             ord.order_id = 1
             ord.item_name = Products.objects.get(name=name)

             #Orders.objects.create(request.user,1,name,False)
             ord.save()
             context = {
                'object':Orders.objects.all()
            }

    return render(request,'orders.html',context)

def cart_view(request):
    context = {
        'count':Orders.objects.filter(user = request.user,status = False).count()
    }
    return render(request,'base.html',context) 

def payment(request):

    return render(request,'payment.html')