from django.shortcuts import render
from .models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.all()   # Fetch all products from DB
    return render(request, 'store/product_list.html', {'products': products})
