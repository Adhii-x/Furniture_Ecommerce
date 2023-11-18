from django.shortcuts import render
from .models import Product,OrderItem,Order,Blog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Other imports...

import stripe
from django.views import View
from django.conf import settings
from django.shortcuts import redirect

# Create your views here.

def index(request):
    context={
        'produ':Product.objects.all(),
        'blog':Blog.objects.all()
    }
    return render(request,'web/index.html',context)


def user_login(request):
    if request.method == "POST":        
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        print('user=',user)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('sign_up')

    return render(request, 'web/account/login.html')


def sign_up(request):
    if request.method=="POST":
        user_name = request.POST.get("username")
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("Confirmpassword")


        if password==confirm_password:

            customer = User.objects.create_user(user_name,email,password)
            customer.first_name= first_name
            customer.last_name= last_name

            customer.save

            return redirect('login')
    return render(request,'web/account/signup.html')


def logout_view(request):
    logout(request)
    return render(request,'web/index.html')
    

@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_details")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_details")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_details")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_details")


@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'web/cart_detail.html')

def checkout(request):
    return render(request,'web/checkout.html')

def placeorder(request):
    if request.method=="POST":
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(id=uid)

        cart=request.session.get('cart')
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")

        country=request.POST.get("country")
        address=request.POST.get("company")
        state=request.POST.get("state")
        pin=request.POST.get("pin")
        phone=request.POST.get("phone")

        order=Order(
            user=user,
            first_name=firstname,
            last_name=lastname,
            country=country,
            address=address,
            state=state,
            pincode=pin,
            phone=phone,
            email=email,
        )
        order.save()

        for i in cart:
            a=float(cart[i]['price'])   
            b=int(cart[i]['quantity'])
            total=a*b

            order1=OrderItem(
                order=order,
                product=cart[i]['name'],
                image=cart[i]['image'],
                price=cart[i]['price'],
                quantity=cart[i]['quantity'],
                total=total

            )
            order1.save()
    return render(request,'web/placeorder.html')


stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateStripeCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price1 = Product.objects.all()
        line_items = []

        for p in price1:
            price2 = p.price
            prod = p.name
            img = p.image.url

            line_item = {
                "price_data": {
                    "currency": "INR",
                    "unit_amount": int(price2) * 100,
                    "product_data": {
                        "name": prod,
                        # You can include img here if needed
                        
                    },
                },
                "quantity": 1,
            }

            line_items.append(line_item)

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url='http://localhost:8000/index.html',
            cancel_url='http://localhost:8000/index.html',
        )



 
   
