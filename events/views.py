from django.shortcuts import render

# Create your views here.
def event(request):
    """ A view to return the event page """

    return render(request, 'events/event.html')