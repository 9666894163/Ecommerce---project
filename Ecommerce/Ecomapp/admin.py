
from django.contrib import admin
from Ecomapp.models import Category, Orders,Products,Customer


# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Orders)