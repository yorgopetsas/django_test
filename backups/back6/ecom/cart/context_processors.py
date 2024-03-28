from .cart import Cart  

#Create context processor 
def cart(request):
    return {'cart': Cart(request)}