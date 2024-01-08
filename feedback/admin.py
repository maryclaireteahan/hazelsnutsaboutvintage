from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'message',
        'date',
    )

    ordering = ('-date',)
    
admin.site.register(Feedback)