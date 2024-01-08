from .models import Feedback
from django import forms

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('subject', 'message')
        
    subject = forms.CharField(
        label='Subject',
        widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'placeholder': 'Message'}))