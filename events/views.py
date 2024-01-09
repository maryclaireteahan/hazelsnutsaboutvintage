from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Event
from .forms import EventForm

# Create your views here.

def all_events(request):
    """ A view to show all events """

    events = Event.objects.all()

    context = {
        'events': events,
        'on_event_page': True,
    }

    return render(request, 'events/events.html', context)


def event_detail(request, slug):
    """ A view to show individual event details """

    event = get_object_or_404(Event, slug=slug)

    context = {
        'event': event,
        'on_event_page': True,
    }

    return render(request, 'events/single_event.html', context)

@login_required
def add_event(request):
    """ Add a events to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('events'))

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Successfully added event!')
            return redirect(reverse('single_event', args=[event.slug]))
        else:
            messages.error(request, 'Failed to add event. Please ensure the form is valid.')
    else:
        form = EventForm()
        
    template = 'events/add_event.html'
    context = {
        'form': form,
        'on_event_page': True,
    }

    return render(request, template, context)


@login_required
def edit_event(request, slug):
    """ Edit a event in the store """
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('events'))

    event = get_object_or_404(Event, slug=slug)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated event!')
            return redirect(reverse('single_event', args=[event.slug]))
        else:
            messages.error(request, 'Failed to update event. Please ensure the form is valid.')
    else:
        form = EventForm(instance=event)
        messages.info(request, f'You are editing {event.title}')

    template = 'events/edit_event.html'
    context = {
        'form': form,
        'event': event,
        'on_event_page': True,
    }

    return render(request, template, context)


@login_required
def delete_event(request, slug):
    """ A view to show individual event details """
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('events'))
    event = get_object_or_404(Event, slug=slug)

    context = {
        'event': event,
        'on_event_page': True,
    }

    return render(request, 'events/event_delete.html', context)
