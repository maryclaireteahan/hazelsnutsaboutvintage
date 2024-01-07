# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views import View
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Event
# from .forms import EventForm




# # Create your views here.

# class Events(View):
#     """
#     View for displaying all events
#     """
#     def get(self, request):
#         events = Event.objects.all()
#         context = {
#             'events': events,
#         }
#         return render(request, 'events/events.html', context)


# class EventDetail(View):
#     """
#     View for displaying a single event
#     """
#     def get(self, request, slug):
#         event = get_object_or_404(Event, slug=slug)
#         context = {
#             'event': event,
#         }
#         return render(request, 'events/single_event.html', context)

# class EventEdit(LoginRequiredMixin, View):
#     """
#     Edit an event
#     """

#     def get(self, request, slug):
#         if request.user.is_superuser:
#             event = get_object_or_404(Event, slug=slug)
#             form = EventForm(instance=event)
#             context = {
#                 'event': event,
#                 'form': form,
#             }
#             return render(request, 'events/edit_event.html', context)
#         else:
#             return render(request, '404.html', status=404)

#     def post(self, request, slug, *args, **kwargs):  # Change event_slug to slug
#         if request.user.is_superuser:
#             event = get_object_or_404(Event, slug=slug)  # Use slug instead of event_slug
#             form = EventForm(request.POST, instance=event)
#             if form.is_valid():
#                 form.save()
#                 return redirect('events:single_event', slug=event.slug)
#             context = {
#                 'event': event,
#                 'form': form,
#             }
#             return render(request, 'events/edit_event.html', context)
#         else:
#             return render(request, '404.html', status=404)



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
    }

    return render(request, 'events/events.html', context)


def event_detail(request, slug):
    """ A view to show individual event details """

    event = get_object_or_404(Event, slug=slug)

    context = {
        'event': event,
    }

    return render(request, 'events/single_event.html', context)


@login_required
def add_event(request):
    """ Add a events to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Successfully added event!')
            return redirect(reverse('event_detail', args=[event.slug]))
        else:
            messages.error(request, 'Failed to add event. Please ensure the form is valid.')
    else:
        form = EventForm()
        
    template = 'events/add_events.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_event(request, slug):
    """ Edit a event in the store """
    on_event_page = True 
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

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
        'on_event_page': on_event_page,
    }

    return render(request, template, context)


@login_required
def delete_event(request, slug):
    """ Delete a event from the store """
    
    on_event_page = True 
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, slug=slug)
    event.delete()
    messages.success(request, 'event deleted!')
    return redirect(reverse('events'))