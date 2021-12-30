from django.contrib import admin

# Register your models here.
from .models import Category, Product, Product_options, Specification

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Product_options)
admin.site.register(Specification)