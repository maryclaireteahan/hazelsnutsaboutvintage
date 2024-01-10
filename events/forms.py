from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    """ Form for adding and editing events """
    class Meta:
        model = Event
        fields = ('title', 'description', 'start_date', 'end_date', 'start_time', 'end_time', 'location',)
        readonly_fields = ('creator','created_on', 'slug',)
        