import uuid

from django.db import models

# Create your models here.
from email.policy import default
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User



# Create your models here.
class Event(models.Model):  
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=200, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=254, default='')

    class Meta:
        """
        Order events from newest to oldest
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns string representation of an object
        """
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)
