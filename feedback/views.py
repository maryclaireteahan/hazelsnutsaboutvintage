from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Feedback
from .forms import FeedbackForm

def feedback(request):
    """ A view to handle feedback submission """
    # Assuming you want to display the latest feedback
    feedback = Feedback.objects.latest('created_at')  # Assuming 'created_at' is the timestamp field
    context = {
        'feedback': feedback,
        'on_feedback_page': True,
    }
    return render(request, 'feedback/feedback.html', context)

def all_feedback(request):
    """ A view to show all feedback """
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            messages.success(request, 'Successfully added feedback!')
        else:
            messages.error(request, 'Failed to add feedback. Please ensure the form is valid.')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        feedback = Feedback.objects.all()  # Get all feedback objects
        context = {
            'feedback': feedback,
            'on_feedback_page': True,
        }
        return render(request, 'feedback/feedback.html', context)

def feedback_detail(request, feedback_id):
    """ A view to show individual feedback details """
    feedback = get_object_or_404(Feedback, pk=feedback_id)
    context = {
        'feedback': feedback,
        'on_feedback_page': True,
    }
    return render(request, 'feedback/feedback_detail.html', context)
