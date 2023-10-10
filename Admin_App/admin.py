from django.contrib import admin
from Admin_App.models import *
# Register your models here.

@admin.register(Brand)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Brand._meta.fields]

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]