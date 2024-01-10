from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    """ Admin view for events """
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
        return qs

admin.site.register(Event, EventAdmin)

