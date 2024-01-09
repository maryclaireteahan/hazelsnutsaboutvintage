from django.contrib import admin
from .models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = (
        'title',
        'location',
        'start_date',
        'end_date',
    )

    ordering = ('-created_on',)

admin.site.register(Event, EventAdmin)

