# from .models import Event
# from django import forms

# class EventForm(forms.ModelForm):
#     """Form for the Event model"""
#     class Meta:
#         model = Event
#         fields = ['name', 'description', 'start_date', 'end_date', 'location',]
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control'}),
#             'start_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
#             'end_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
#             'location': forms.TextInput(attrs={'class': 'form-control'}),
#         }