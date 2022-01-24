from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.
from django.shortcuts import render
from .models import *

# Create your views here.

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
        form = Registration_user()        
    return render(request,'register.html',{'form':form})

def Login(request):
    if request.method == 'POST':
        U = request.POST['username']
        P = request.POST['password']
        obj = authenticate(request,username =U,Password = P)
        if obj is not None:
            login(request,obj)
            return redirect('home')
        else:
            messages.error(request,'something went wrong')

    else:
        return render(request,'login.html')    
