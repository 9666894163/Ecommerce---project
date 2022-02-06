from datetime import datetime
import email
from pickle import TRUE
from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length= 20)
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to = 'images')

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=25)   
    last_name = models.CharField(max_length=25) 
    phone = models.IntegerField() 
    email = models.EmailField()
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.first_name

class Orders(models.Model):
    order_id = models.IntegerField()
    user = models.CharField(max_length=25) 
    item_name= models.ForeignKey(Products,on_delete=models.CASCADE)  
    status = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return str(self.item_name) + str(self.order_id)

