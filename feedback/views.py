from django.shortcuts import render

from .models import Feedback
from .forms import FeedbackForm

def feedback(request):
    """ A view to return the feedback page """
    
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            return render(request, 'home/index.html')
    else:
        feedback_form = FeedbackForm()
        
    context = {
        'feedback_form': feedback_form,
    }
    
    return render(request, 'feedback/feedback.html', context)
