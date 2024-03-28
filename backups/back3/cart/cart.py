from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get the current session key if it exists
        cart = self.session.get('session_key')

        #If the user is new, create seassion key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        # make sure cart is available on all pages
        self.cart = cart
    
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        # Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)
        
        self.session.modified = True
    
    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        #Get ids from cart
        product_ids = self.cart.keys()
        #Use id to look up products and db models
        products = Product.objects.filter(id__in=product_ids)

        return products

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        our_cart = self.cart

        # Update Dictionary/cart
        our_cart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing

    def delete(self, product):
        product_id = str(product)

        # Delete from dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True
    
    def totals(self):
        # Get Products IDS
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        quantities = self.cart

        cart_total = 0

        for k,v in quantities.items():
            k = int(k)
            for product in products:
                if product.id == k and product.sale:
                    cart_total += product.sale_price * v
                elif product.id == k:
                    cart_total += product.price * v
        return cart_total
