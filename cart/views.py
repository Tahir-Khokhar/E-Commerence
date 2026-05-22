from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .cart import Cart

def cart_add(request, product_id):
    """Add product to cart"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    """Remove product from cart"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    """Show cart page"""
    cart = Cart(request)
    return render(request, 'cart/cart_details.html', {'cart': cart})
