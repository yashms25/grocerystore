from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Offer


# Create your views here.


def index(request):
    cart = request.session.get('cart')

    if not cart:
        request.session['cart'] = {}
    products = Product.objects.all()
    # return HttpResponse('Hello, Welcome to the project')
    product = request.POST.get('product')
    remove = request.POST.get('remove')
    if product is not None:
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
    return render(request, 'index.html', {'products': products})


def cart(request):
    if request.method == 'POST':
        codes = ''
        codes = request.POST.get('getcode')
        offers = Offer.objects.all()
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request, 'cart.html', {'products': products, 'offers': offers, 'codes': codes})
    else:
        codes = ''
        codes = request.POST.get('getcode')
        offers = Offer.objects.all()
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request, 'cart.html', {'products': products, 'offers': offers, 'codes': codes})


def thank_you(request):
    if request.method == 'POST':
        request.session['cart'] = {}
        return redirect('/')
    else:
        return render(request, 'Thank you.html')
