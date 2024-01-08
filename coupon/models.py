import uuid


from django.db import models

# Create your models here.
class Coupon(models.Model):
    """ A model for coupon """
    code = models.CharField(max_length=20, unique=True)
    barcode_image = models.ImageField(upload_to='barcode_images', blank=True, null=True)    
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def _generate_order_number(self):
        """ Generate a random, unique order number using UUID """
        return uuid.uuid4().hex.upper()
    
    class Meta:
        verbose_name_plural = 'Coupon'
    def __str__(self):
        return self.code
    
    class Meta:
        """
        Order posts from newest to oldest
        """
        ordering = ['-created_on']
        
