from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Product_options(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    quantity = models.IntegerField()
    weight = models.FloatField()
    price = models.IntegerField()
    def __str__(self):
        return self.color

class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    battery = models.CharField(max_length=50)
    camera = models.CharField(max_length=50)
    def __str__(self):
        return self.model
