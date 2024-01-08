from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Feedback
from .forms import FeedbackForm

def feedback(request):
    """ A view to handle feedback submission """
    
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            messages.success(request, 'Successfully added feedback!')
            return redirect(reverse('home'))  # Redirect to the home page after adding feedback
        else:
            messages.error(request, 'Failed to add feedback. Please ensure the form is valid.')
    else:
        feedback_form = FeedbackForm()
        
    context = {
        'feedback_form': feedback_form,
    }
    
    return render(request, 'feedback/feedback.html', context)


def all_feedback(request):
    """ A view to show all feedback """

    feedback = Feedback.objects.all()

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
