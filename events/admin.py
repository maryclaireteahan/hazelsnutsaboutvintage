from django.contrib import admin

# Register your models here.
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
    list_filter = ('start_date', 'end_date',) 

    ordering = ('-created_on',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Check if any filters are applied here unintentionally
        return qs
    
admin.site.register(Event, EventAdmin)

