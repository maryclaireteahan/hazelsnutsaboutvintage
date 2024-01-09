from django.contrib import admin
from .models import Coupon

class CouponAdmin(admin.ModelAdmin):
    """ Admin view for coupon """
    list_display = ('code','description', 'created_on',)
    readonly_fields = ('created_on',)

    ordering = ('-created_on',)

    fields = ('code', 'discount', 'description', 'created_on', )


admin.site.register(Coupon)
