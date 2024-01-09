from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Coupon

def coupon(request):
    """ A view to return the coupon page """
    coupons = Coupon.objects.all()  
    context = {
        'coupons': coupons  
    }
    return render(request, 'coupon/coupon.html', context)
