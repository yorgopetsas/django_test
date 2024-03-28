from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.totals()
    return render(request, "cart_summary.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals})

def cart_add(request):
    # Get the cart
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        # Look up product in the db
        product = get_object_or_404(Product, id=product_id)
        # Save to session
        cart.add(product=product, quantity=product_qty)

        # Get Qty
        cart_quantity = cart.__len__()
        # Return response
        # response = JsonResponse({'Product name': product.name})
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, ("Product added to the cart!"))
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        # call delete function in cart 
        cart.delete(product_id)
        response = JsonResponse({'product':product_id})
        messages.success(request, ("Product deleted"))
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantities=product_qty)
        response = JsonResponse({'qty':product_qty})
        messages.success(request, ("Product quantity updated. New quantity {{ product_qty }}"))
        return response

