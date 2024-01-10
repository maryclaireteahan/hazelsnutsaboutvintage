from django.db import models


class Feedback(models.Model):
    """ A model for feedback """
    subject = models.CharField(max_length=254, default='')
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Feedback'

    def __str__(self):
        return self.subject

    class Meta:
        """
        Order posts from newest to oldest
        """
        ordering = ['-created_on']
