
from email import header
import uuid

from django.db import models

class Coupon(models.Model):
    header = models.CharField(max_length=200, null=False, blank=False, default='')
    code = models.CharField(max_length=32, null=False, editable=False)
    created_on = models.DateField(auto_now_add=True, null=True, blank=True)
    description = models.TextField(max_length=255, null=False, blank=False, default='')

    def __str__(self):
        return self.code
    
    def _generate_code(self):
        """ Generate a random, unique code using UUID """
        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):
        """ Override the original save method to set the code if it hasn't been set already """
        if not self.code:
            self.code = self._generate_code()
        super().save(*args, **kwargs)
    