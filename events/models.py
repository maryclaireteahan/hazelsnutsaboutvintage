from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images')
    slug = models.SlugField()
    
    def __str__(self):
        return self.name