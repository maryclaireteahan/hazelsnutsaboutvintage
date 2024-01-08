import uuid
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Coupon, CouponCode, CouponBarcode
from .utils import generate_barcode_image


# Create your views here.
def coupon(request):
    """ A view to return the index page """
    coupons = Coupon.objects.all()
    return render( request,'coupon/coupon.html', {'coupons': coupons})
# coupon/views.py


def generate_coupon(request, order_number):
    # Generate or retrieve the coupon based on the order number
    coupon_description = f"Coupon for order {order_number}"
    
    # Check if a coupon with the same order number exists
    existing_coupon = Coupon.objects.filter(description=coupon_description).first()

    if existing_coupon:
        # Return the existing coupon code associated with the order number
        coupon_code = existing_coupon.code
    else:
        # Generate a new code and create a coupon with the order number's description
        new_coupon_code = uuid.uuid4().hex.upper()[:8]  # Generate a random 8-character code

        coupon, created = Coupon.objects.get_or_create(
            description=coupon_description,
            defaults={'code': new_coupon_code}
        )

        if created or not coupon.barcode_image:
            barcode_filepath = generate_barcode_image(new_coupon_code)
            coupon.barcode_image = barcode_filepath
            coupon.save()

        coupon_code = coupon.code

    return HttpResponse(f"Coupon code for order {order_number}: {coupon_code}")
