
from shortuuidfield import ShortUUIDField

from django.db import models

class Coupon(models.Model):
    header = models.CharField(max_length=200, null=False, blank=False, default='')
    code = ShortUUIDField(max_length=22, null=False, editable=False)
    created_on = models.DateField(auto_now_add=True, null=True, blank=True)
    description = models.TextField(max_length=255, null=False, blank=False, default='')

    def __str__(self):
        return self.code
# 