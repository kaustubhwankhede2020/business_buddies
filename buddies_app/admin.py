from django.contrib import admin
from buddies_app import models

# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Product)