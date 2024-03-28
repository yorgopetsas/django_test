from django.contrib import admin
from .models import Category, Customer, Product, Order, Profile, Service, Discount
from django.contrib.auth.models import User

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)
admin.site.register(Service)
admin.site.register(Discount)

# Mix profile info and user info

class ProfileInline(admin.StackedInline):
    model = Profile

# Extend User Model
    
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name", "email",]
    inlines = [ProfileInline]

# Unregister old way user
admin.site.unregister(User)

# Re-register with new user
admin.site.register(User, UserAdmin)