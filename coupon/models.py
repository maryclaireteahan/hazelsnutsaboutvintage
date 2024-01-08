from os import name
import uuid


from django.db import models

# Create your models here.
class Coupon(models.Model):
    """ A model for coupon """
    name = models.CharField(max_length=254, default='')
    barcode_image = models.ImageField(upload_to='barcode_images', blank=True, null=True)    
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def _generate_code():
        """ Generate a random, unique order number using UUID """
        return uuid.uuid4().hex.upper()

    code = models.CharField(max_length=32, unique=True, default=_generate_code, editable=False)

    class Meta:
        verbose_name_plural = 'Coupon'
    def __str__(self):
        return self.code
    
