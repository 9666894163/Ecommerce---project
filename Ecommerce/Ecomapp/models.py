from django.db import models

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