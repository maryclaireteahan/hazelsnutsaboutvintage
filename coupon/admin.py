from django.contrib import admin
from .models import Coupon

class CouponAdmin(admin.ModelAdmin):
    """ Admin view for coupon """
    list_display = ('name', 'description', 'created_on')
    readonly_fields = ('created_on',)

    ordering = ('-created_on',)

    fields = ('name', 'description', 'created_on')


admin.site.register(Coupon)
