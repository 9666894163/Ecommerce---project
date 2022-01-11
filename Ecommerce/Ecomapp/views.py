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