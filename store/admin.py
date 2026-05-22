from django.contrib import admin
from .models import Product

# Register your models here.

# Register Product model so it appears in Django admin
admin.site.register(Product)
