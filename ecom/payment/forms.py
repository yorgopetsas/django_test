from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-contro', 'placeholder': 'Full Name'}), required=True)
    shipping_email = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-contro', 'placeholder': 'Email'}), required=True)
    shipping_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-contro', 'placeholder': 'Address1'}), required=True)
    shipping_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-contro', 'placeholder': 'Address2'}), required=True)
    shipping_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-contro', 'placeholder': 'City'}), required=True)
    shipping_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-contro', 'placeholder': 'State'}), required=False)
    shipping_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-contro', 'placeholder': 'Zip Code'}), required=False)
    shipping_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-contro', 'placeholder': 'Country'}), required=True)

    class Meta:
        model = ShippingAddress
        fields = ["shipping_full_name", "shipping_email", "shipping_address1", "shipping_address2", "shipping_city", "shipping_state", "shipping_zipcode", "shipping_country"]

        exclude = ['user',]

class PaymentForm(forms.Form):
    card_name =forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-contro', 'placeholder': 'Name on Card'}), required=True)
    card_number =forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-contro', 'placeholder': 'Card Number'}), required=True)
    card_exp_date =forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-contro', 'placeholder': 'Expiration Date'}), required=True)
    card_cvv_number =forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-contro', 'placeholder': 'CVV Number'}), required=True)
    card_address1 =forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-contro', 'placeholder': 'Card Address 1'}), required=True)
    card_address2 =forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-contro', 'placeholder': 'Card Address 2'}), required=False)
    card_city =forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-contro', 'placeholder': 'Card City'}), required=True)
    card_state =forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-contro', 'placeholder': 'Card State'}), required=True)
    card_zipcode =forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-contro', 'placeholder': 'Card Postal Code'}), required=True)
    card_country =forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-contro', 'placeholder': 'Card Country'}), required=True)