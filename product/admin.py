from django.contrib import admin
from .models import Country, Product, Category, City, Subcategory
# Register your models here.

admin.site.register(Product)
admin.site.register(Country)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Subcategory)