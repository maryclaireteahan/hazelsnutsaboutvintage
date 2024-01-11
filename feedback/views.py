from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Feedback
from .forms import FeedbackForm

@login_required
def feedback(request):
    """ A view to handle feedback submission """
    feedback = Feedback.objects.latest('created_at')
    context = {
        'feedback': feedback,
        'on_feedback_page': True,
    }
    return render(request, 'feedback/feedback.html', context)

@login_required
def all_feedback(request):
    """ A view to show all feedback """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            messages.success(request, 'Successfully added feedback!')
        else:
            messages.error(request,
                           'Failed to add feedback.'
                           'Please ensure the form is valid.')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        feedback = Feedback.objects.all()  # Get all feedback objects
        context = {
            'feedback': feedback,
            'on_feedback_page': True,
        }
        return render(request, 'feedback/feedback.html', context)

@login_required
def feedback_detail(request, feedback_id):
    """ A view to show individual feedback details """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    feedback = get_object_or_404(Feedback, pk=feedback_id)
    context = {
        'feedback': feedback,
        'on_feedback_page': True,
    }
    return render(request, 'feedback/feedback_detail.html', context)
