from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem, OrderStatus

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name',  "date_ordered", 'amount_paid')
#     def customer_name(self, obj):
#         return obj.customer.name
#     customer_name.admin_order_field = 'user'
#     def order_date(self, obj):
#         return obj.date_created.strftime('%Y-%m-%d %H:%M:%S')
#     order_date.short_description = 'Order Date'
#     def total_amount(self, obj):
#         return obj.calculate_total_amount()
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'id', 'product', 'user', 'quantity', 'price')


admin.site.register(Order, OrderAdmin)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(OrderStatus)
