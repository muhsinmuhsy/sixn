from django.contrib import admin
from Auth_App.models import User, Distributor

# Register your models here.

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'is_superuser', 'is_salesmanager', 'is_purchasemanager', 'is_distributor', 'email', 'phone', 'place' ]


@admin.register(Distributor)
class DistributorModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Distributor._meta.fields]