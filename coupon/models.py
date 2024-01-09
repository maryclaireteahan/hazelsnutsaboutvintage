
        
from os import name
import uuid


from django.db import models

# # Create your models here.
# class CouponCode(models.Model):
#     """ A model for coupon code """
    
#     def _generate_code():
#         """ Generate a random, unique order number using UUID """
#         return uuid.uuid4().hex.upper()
    
#     code = models.CharField(max_length=32, unique=True, default=_generate_code, editable=False)
    
#     class Meta:
#         verbose_name_plural = 'Coupon Code'
#     def __str__(self):
#         return self.code

# class CouponBarcode(models.Model):
#     """ A model for coupon barcode """
#     barcode_image = models.ImageField(upload_to='barcode_images', blank=True, null=True)

class Coupon(models.Model):
    """ A model for coupon """
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    created_on = models.DateField(auto_now_add=True, null=True, blank=True)
    barcode_image = models.ImageField(upload_to='barcode_images', blank=True, null=True)
    code = models.CharField(max_length=32, null=False, editable=False)


    def _generate_code(self):
        """ Generate a random, unique order number using UUID """
        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):
        """ Override the original save method to set the order number if it hasn't been set already """
        if not self.code:
            self.code = self._generate_code()
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = 'Coupon'
    def __str__(self):
        return self.name
            