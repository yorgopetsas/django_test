from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from colorfield.fields import ColorField
from django.db.models.signals import post_save


class ShippingAddress(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_full_name = models.CharField(max_length=255)
    shipping_email = models.CharField(max_length=255)
    shipping_address1 = models.CharField(max_length=255)
    shipping_address2 = models.CharField(max_length=255)
    shipping_city = models.CharField(max_length=255)
    shipping_state = models.CharField(max_length=255, null=True, blank=True)
    shipping_zipcode = models.CharField(max_length=255, null=True, blank=True)
    shipping_country = models.CharField(max_length=255)

    # Don't plurize address
    class Meta:
        verbose_name_plural = "Shipping Address"

    def __str__(self):
        return f'Shipping Address - {str(self.id)}'

# def create_shipping(sender, instance, created, **kwargs):
#     if created:
#         user_shipping = ShippingAddress(user=instance)
#         user_shipping.save()

# post_save.connect(create_shipping, sender=User)

# Create a user Shipping Address by default when user signs up
def create_shipping(sender, instance, created, **kwargs):
	if created:
		user_shipping = ShippingAddress(user=instance)
		user_shipping.save()

# Automate the profile thing
post_save.connect(create_shipping, sender=User)

class OrderStatus(models.Model):

    status_name = models.CharField(max_length=100)
    status_visible = models.BooleanField(default=False)
    status_color = ColorField()
    status_send_email = models.BooleanField(default=False)
    status_email_template = models.CharField(max_length=100)
    status_paid = models.BooleanField(default=False)
    status_sent = models.BooleanField(default=False)
    status_delivered = models.BooleanField(default=False)
    status_attach_file = models.BooleanField(default=False)
    status_file_url = models.URLField()
    status_hide_for_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.status_name)

    class Meta:
        verbose_name_plural = "OrderStatuses"

# Create order Model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    order_shipping_address = models.ForeignKey(ShippingAddress,  on_delete=models.CASCADE, null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=9, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.id)
        # return f'Order - {str(self.id)}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=9, decimal_places=2)    

    def __str__(self):
        return f'Order Item - {str(self.id)}'
