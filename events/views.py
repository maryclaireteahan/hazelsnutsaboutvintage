from multiprocessing import context
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from requests import post
from .models import Event
from django.http import HttpResponseRedirect
# from .forms import EventForm

# Create your views here.


class EventDetail(View):
    """
    View for displaying event details
    """
    def get(self, request, slug):
        event = get_object_or_404(Event, slug=slug)    
        context = {
            'event': event,
        }
        
        return render(request, 'event.html', context)
    
    
    
    
    

# class EventCreate(LoginRequiredMixin, View):
#     """
#     View for allowing superusers to create events on the frontend
#     """
#     def get(self, request):
#         if request.user.is_superuser:
#             form = EventForm()
#             return render(request, 'admin_event_create.html',
#                           {'event_form': form})
#         else:
#             return render(request, '404.html', status=404)

#     def post(self, request, *args, **kwargs):
#         if request.user.is_superuser:
#             event_form = EventForm(request.POST, request.FILES)
#             if event_form.is_valid():
#                 event = event_form.save(commit=False)
#                 event.slug = event.title.replace(" ", "-").lower()
#                 event.email = 'admin'
#                 event.name = 'admin'
#                 event.user = request.user
#                 event.save()
#                 return HttpResponseRedirect(reverse('event',
#                                                     args=[event.slug]))
#             else:
#                 event_form = EventForm()
#             return render(
#                 request,
#                 'admin_event_create.html',
#                 {
#                     'event_form': EventForm()
#                 },
#             )
#         else:
#             return render(request, '404.html', status=404)


# @login_required
# def eventEdit(request, id):
#     """
#     View for allowing superusers to edit events on the frontend
#     """
#     event_instance = get_object_or_404(Event, id=id)
#     form = EventForm(request.POST or None,
#                       request.FILES or None, instance=event_instance)
#     if request.user.is_authenticated and request.user.is_superuser:
#         if request.method == "POST":
#             form = EventForm(request.POST, instance=event_instance)
#             if form.is_valid():
#                 try:
#                     form.save()
#                     return redirect('/event')
#                 except Exception as e:
#                     pass
#         return render(request, 'admin_event_edit.html', {'form':form})
#     else:
#         return render(request, '404.html', status=404)


# @login_required
# def eventDelete(request, id):
#     """
#     View for allowing superusers to delete events on the frontend
#     """
#     event_instance = get_object_or_404(Event, id=id)
#     if request.user.is_authenticated and request.user.is_superuser:
#         if request.method == 'POST':
#             event_instance.delete()
#             return redirect('/event')
#         else:
#             return render(request, 'admin_event_delete.html',
#                           {'event_instance': event_instance})
#     else:
#         return render(request, '404.html', status=404)
