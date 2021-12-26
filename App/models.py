from django.db import models

# Create your models here.
class Category(models.Model):
    apple = models.CharField(max_length=50)
    samsung = models.CharField(max_length=50)
    xiomi = models.CharField(max_length=50)
    huawei = models.CharField(max_length=50)

class Product(models.Model):
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Product_options(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    quantity = models.IntegerField()
    weight = models.FloatField()
    price = models.IntegerField()

class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    battery = models.CharField(max_length=50)
    camera = models.CharField(max_length=50)
