from django.shortcuts import render
from shop.models.Cart import Cart, CartItem


def main_view(request):
    return render(request, "shop/Main.html", {'cart': Cart.get_from_request(request)})
