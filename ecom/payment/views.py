from django.shortcuts import render
from cart.cart import Cart
from .forms import ShippingForm
from .models import ShippingAddress

def checkout(request):
     # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.totals()

    shipping_user = ShippingAddress.objects.get(user__id=request.user.id)

    if request.user.is_authenticated:
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(request, "payment/checkout.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals, "shipping_form": shipping_form})
    else:
        # Checkout as guest
        shipping_form = ShippingForm(request.POST or None)
        return render(request, "payment/checkout.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals})

def payment_success(request):
    return render(request, "payment/payment_success.html", {})
