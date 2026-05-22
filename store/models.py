from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)   # Product name
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price
    description = models.TextField()          # Product description
    stock = models.IntegerField()             # Available stock

    def __str__(self):
        return self.name   # Show product name in admin panel
