from django.db import models

# Create your models here.
class Category(models.Model):
    """ A category for a product"""
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.name
        
    def get_friendly_name(self):
        return self.friendly_name
    
class Brand(models.Model):
    """ A brand for a product"""    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.name
        
    def get_friendly_name(self):
        return self.friendly_name

class Size(models.Model):
    """ A size for a product """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.name
        
    def get_friendly_name(self):
        return self.friendly_name
    
class Product(models.Model):
    """ Database model for adding products to the store"""
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_alt = models.CharField(max_length=254, default='image alt')
    size = models.ForeignKey('Size', null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.image_alt = self.name 
        super().save(*args, **kwargs)