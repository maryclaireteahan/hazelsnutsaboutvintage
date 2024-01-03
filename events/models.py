from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=254, default='')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name