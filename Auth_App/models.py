from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_salesmanager = models.BooleanField(default=False)
    is_purchasemanager = models.BooleanField(default=False)
    is_distributor = models.BooleanField(default=False)
    image = models.ImageField(upload_to='user-images' ,null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)

class Distributor(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    EDUCATION = (
        ('SSLC', 'SSLC'),
        ('Plus Two', 'Plus Two'),
        ('Degree', 'Degree'),
        ('PG', 'PG'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='distributor_profile')
    blood_group = models.CharField(max_length=15, null=True, blank=True)
    whatsapp_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=15, choices=GENDER, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address_one = models.CharField(max_length=150, null=True, blank=True)
    address_two = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    district = models.CharField(max_length=50, null=True, blank=True)
    education = models.CharField(max_length=25, null=True, blank=True, choices=EDUCATION)
    education_description = models.CharField(max_length=250, null=True, blank=True)
    father_name = models.CharField(max_length=50, null=True, blank=True)
    father_number = models.CharField(max_length=50, null=True, blank=True)
    father_job = models.CharField(max_length=50, null=True, blank=True)
    mother_name = models.CharField(max_length=50, null=True, blank=True)
    mother_number = models.CharField(max_length=50, null=True, blank=True)
    mother_job = models.CharField(max_length=50, null=True, blank=True)
    friend_one_name = models.CharField(max_length=50, null=True, blank=True)
    friend_one_number = models.CharField(max_length=50, null=True, blank=True)
    friend_one_job = models.CharField(max_length=50, null=True, blank=True)
    friend_two_name = models.CharField(max_length=50, null=True, blank=True)
    friend_two_number = models.CharField(max_length=50, null=True, blank=True)
    friend_two_job = models.CharField(max_length=50, null=True, blank=True)
    distribution_area = models.CharField(max_length=50, null=True, blank=True)
    aadhaar_number = models.CharField(max_length=50, null=True, blank=True)
    aadhaar_image = models.ImageField(upload_to='aadhaar-image', null=True, blank=True)
    pan_card_number = models.CharField(max_length=50, null=True, blank=True)
    pan_card_image = models.ImageField(upload_to='pan-card-image', null=True, blank=True)
    bank_name = models.CharField(max_length=50, null=True, blank=True)
    bank_branch_name = models.CharField(max_length=50, null=True, blank=True)
    bank_holder_name = models.CharField(max_length=50, null=True, blank=True)
    bank_account_number = models.CharField(max_length=50, null=True, blank=True)   
    bank_ifc_code =models.CharField(max_length=50, null=True, blank=True)
    



