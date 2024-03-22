from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    return render(request, "cart_summary.html", {})

def cart_add(request):
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = request.POST.get('product_id')
        # look up product in the db
        product = get_object_or_404(Product, id=product_id)
        # Save to session
        cart.add(product=product)
        # Return response
        response = JsonResponse({'Product name': product.name})
        return response
    # return render(request, "cart_add.html")

def cart_delete(request):
    return render(request, "cart_delete.html")

def cart_update(request):
    return render(request, "cart_update.html")
