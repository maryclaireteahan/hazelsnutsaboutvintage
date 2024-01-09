import secrets
from django.views.decorators.cache import cache_control
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Coupon
from .utils import generate_barcode_image

from django.shortcuts import get_object_or_404

def coupon(request, coupon_code):
    """ A view to return the coupon page """
    coupon = get_object_or_404(Coupon, code=coupon_code)
    return render(request, 'coupon/coupon.html', {'coupon': coupon})

