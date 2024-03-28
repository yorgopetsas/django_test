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

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f'Order Item - {str(self.id)}'


# Create order Model
class Order(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    shipping_address = models.TextField(max_length=15000)
    amount_paid = models.DecimalField(max_digits=9, decimal_places=2)

    date_ordered = models.DateTimeField(auto_now_add=True)
    
    order_status = models.OneToOneField(OrderStatus, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.id)