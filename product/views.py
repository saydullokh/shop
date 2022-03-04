from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from shop.models import ProductModel


@login_required
def update_wishlist(request, pk):
    product = get_object_or_404(ProductModel.objects.get(pk))
    wishlist = WishListModel.add_to_delete(request.user, product)
