from django.db import models

# Create your models here.
class Feedback(models.Model):
    """ A model for feedback """
    subject = models.CharField(max_length=254, default='')
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Feedback'
    def __str__(self):
        return self.subject
    
    