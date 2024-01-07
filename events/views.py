from multiprocessing import context
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from requests import post
from .models import Event
from django.http import HttpResponseRedirect
from .forms import EventForm

# Create your views here.

class Events(View):
    """
    View for displaying all events
    """
    def get(self, request):
        events = Event.objects.all()
        context = {
            'events': events,
        }
        return render(request, 'events/events.html', context)


class EventDetail(View):
    """
    View for displaying a single event
    """
    def get(self, request, slug):
        event = get_object_or_404(Event, slug=slug)
        context = {
            'event': event,
        }
        return render(request, 'events/single_event.html', context)
    
class EventEdit(LoginRequiredMixin, View):
    """
    View for editing a single event
    """
    def get(self, request, slug):
        event = get_object_or_404(Event, slug=slug)
        context = {
            'event': event,
        }
        return render(request, 'events/edit_event.html', context)
    
    def post(self, request, slug):
        event = get_object_or_404(Event, slug=slug)
        event.title = request.POST['title']
        event.description = request.POST['description']
        event.start_date = request.POST['start_date']
        event.end_date = request.POST['end_date']
        event.start_time = request.POST['start_time']
        event.end_time = request.POST['end_time']
        event.location = request.POST['location']
        event.save()
        return HttpResponseRedirect(reverse('single_event', args=[event.slug]))