from django.contrib import admin
from .models import Category, Customer, Product, Profile, Service, Discount, Brand
from django.contrib.auth.models import User
#
from django import forms
from django.forms.models import BaseInlineFormSet

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Service)
admin.site.register(Discount)

class DiscountChoiceInlineFormSet(BaseInlineFormSet):
    pass

class ProfileInline(admin.StackedInline):
    model = Profile
    
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name", "email",]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)