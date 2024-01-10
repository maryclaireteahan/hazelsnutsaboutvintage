# Register your models here.
from django.contrib import admin
from .models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = (
        'creator',
        'title',
        'location',
        'start_date',
        'end_date',
    )
    list_filter = ('start_date', 'end_date',) 

    ordering = ('-created_on',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Print the SQL query for debugging (optional)
        print(qs.query)
        return qs

admin.site.register(Event, EventAdmin)

