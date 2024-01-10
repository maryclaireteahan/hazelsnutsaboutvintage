from django.contrib import admin
from .models import Product, Category, Brand, Size


class ProductAdmin(admin.ModelAdmin):
    """ Admin view for products """
    list_display = (
        'sku',
        'name',
        'size',
        'category',
        'brand',
        'price',
        'image',
    )

    ordering = ('sku',)

    def get_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])


class CategoryAdmin(admin.ModelAdmin):
    """ Admin view for categories """
    list_display = (
        'friendly_name',
        'name',
    )


class BrandAdmin(admin.ModelAdmin):
    """ Admin view for brands """
    list_display = (
        'friendly_name',
        'name',
    )


class SizeAdmin(admin.ModelAdmin):
    """ Admin view for sizes """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
