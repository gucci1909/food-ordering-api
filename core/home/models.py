from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, default='Umang')
    age= models.IntegerField(default=0)
    email= models.EmailField(null=True, blank=True)
    
class Product(models.Model):
    product_name= models.CharField(max_length=100, default='Unnamed Product')
    product_price=models.IntegerField(default=0)
