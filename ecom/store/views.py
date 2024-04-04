from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from django import forms
#query multiple things
from django.db.models import Q
import json
from cart.cart import Cart

def search(request):
    # Form Filled?
    if request.method == "POST":
        search_term = request.POST['search_term']
        # Query the products db model
        search_term = Product.objects.filter(Q(name__icontains=search_term) | Q(description__icontains=search_term))
        # Test for null
        if not search_term:
            messages.success(request, "Search returned 0 results...")
            return render(request, "search.html", {})
        else:
            return render(request, "search.html", {"search_term": search_term})
    else:
        return render(request, "search.html", {})

def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        # Get Shippin address
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)

        form = UserInfoForm(request.POST or None, instance=current_user)
        ## Ger user shipping form
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        if  form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()
            messages.success(request, "Your info has been updated!")
            return redirect('home')

        # return render(request, "update_info.html", {"form":form})
        return render(request, "update_info.html", {'form': form, 'shipping_form': shipping_form})
    else:
        messages.success(request, "You must be logged in to access this page")
        return redirect('home')

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your Password has been updated")
                login(request, current_user)
                return redirect("update_user")
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect("update_password")
        else:
            form = ChangePasswordForm(current_user)
            return render(request, "update_password.html", {"form": form})
    else:
        messages.success(request, "You must be logged in to see that pagePassword has been updated")
        return redirect("home")

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, "User has been updated!")
            return redirect('home')
        
        return render(request, "update_user.html", {'user_form': user_form})
    else:
        messages.success(request, "You must be logged in to access this page")
        return redirect('home')

def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products":products})

def about(request):
    return render(request, "about.html", {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Add old_cart values
            current_user = Profile.objects.get(user__id=request.user.id)
            saved_cart = current_user.old_cart
            # Convert db string to python dictionary
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                # Add the dict to the session
                cart = Cart(request)
                # Loop and add items
                for product, quantity in converted_cart.items():
                    cart.db_add(product=product, quantity=quantity)

            messages.success(request, ("You have been logged in"))
            return redirect('home')
        else:
            messages.success(request, ("Login errror, please try again"))
            return redirect('login')
    else:
        return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect("home")

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user Have to disable
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("User Created, please finish your registration."))
            return redirect("upadte_info")
        else:
            messages.success(request, ("Something went wrong, please try again."))
            return redirect("register")
    else:
        return render(request, "register.html", {'form':form})

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product.html", {"product":product})

def category(request, foo):
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})
    except:
        messages.success(request("That Category does not exist"))
        return redirect('home')
    

def brand(request, foo):
    foo = foo.replace('-', ' ')
    try:
        brand = Category.objects.get(name=foo)
        products = Product.objects.filter(brand=brand)
        return render(request, 'brands.html', {'products':products, 'brand':brand})
    except:
        messages.success(request("That Brand does not exist"))
        return redirect('home')
    
def category_summary(request):
    categories = Category.objects.all()
    return render(request, "category_summary.html", {"categories": categories})

# def create_order(request):
#     products = 
#     client = 
#     status = "NewOrder"