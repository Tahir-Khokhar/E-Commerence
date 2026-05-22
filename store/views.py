from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q

def home(request):
    """Homepage - Featured products"""
    products = Product.objects.filter(available=True)[:8]
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories
    })

def product_list(request, category_slug=None):
    """List products with optional category filter"""
    products = Product.objects.filter(available=True)
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'store/product_list.html', {
        'products': products,
        'category': category
    })

def product_detail(request, slug):
    """Product detail page"""
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'store/product_detail.html', {'product': product})



def product_list(request, category_slug=None):
    products = Product.objects.filter(available=True)
    category = None
    query = request.GET.get('q', '')

    # Search
    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query)
        )

    # Category Filter
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Price Filter
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    categories = Category.objects.all()

    return render(request, 'store/product_list.html', {
        'products': products,
        'category': category,
        'categories': categories,
        'query': query
    })
