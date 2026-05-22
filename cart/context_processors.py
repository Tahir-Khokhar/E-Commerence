from .cart import Cart


def cart(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return {'cart': cart, 'cart_total': total, 'cart_count': len(cart)}


def cart(request):
    """Make cart available in all templates"""
    return {'cart': Cart(request)}