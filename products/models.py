from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """ A category for a product"""
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ Returns the name of the category """
        return self.name

    def get_friendly_name(self):
        """ Returns the friendly name of the category """
        return self.friendly_name


class Brand(models.Model):
    """ A brand for a product"""
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ Returns the name of the brand """
        return self.name

    def get_friendly_name(self):
        """ Returns the friendly name of the brand """
        return self.friendly_name


class Size(models.Model):
    """ A size for a product """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ Returns the name of the size """
        return self.name

    def get_friendly_name(self):
        """ Returns the friendly name of the size """
        return self.friendly_name


class Product(models.Model):
    """ Database model for adding products to the store"""
    category = models.ForeignKey('Category',
                                 null=True, blank=True,
                                 on_delete=models.SET_NULL)
    brand = models.ForeignKey('Brand',
                              null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=False, blank=False)
    image = CloudinaryField('image', null=True, blank=True)
    image_alt = models.CharField(max_length=254, default='image alt')
    size = models.ForeignKey('Size', null=True,
                             blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        """ Returns the name of the product """
        return self.name

    def save(self, *args, **kwargs):
        """
        Overrides the original save method to set the
        image_alt field to the product name
        """
        self.image_alt = self.name
        super().save(*args, **kwargs)
