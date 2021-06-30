from django.db import models

# Create your models here.
class Customer(models.Model):
    main_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    email = models.EmailField()
    mobile_no_1 = models.CharField(max_length=15)
    mobile_no_2 = models.CharField(max_length=15)
    mobile_no_3 = models.CharField(max_length=15)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    address = models.TextField()
    profession = models.CharField(max_length=50)
    customer_source = models.CharField(max_length=20)
    description = models.TextField()
    additional_notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    main_id = models.AutoField(primary_key=True)
    product_title = models.CharField(max_length=100)
    product_desc = models.TextField()
    listing_unit_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Sale(models.Model):
    main_id = models.AutoField(primary_key=True)

class Scheduling(models.Model):
    main_id = models.AutoField(primary_key=True)

class Payment(models.Model):
    main_id = models.AutoField(primary_key=True)

class Session(models.Model):
    main_id = models.AutoField(primary_key=True)

class Expense(models.Model):
    main_id = models.AutoField(primary_key=True)

