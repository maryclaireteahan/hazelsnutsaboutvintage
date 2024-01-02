from django.shortcuts import render

# Create your views here.
def event(request):
    """ A view to return the index page """

    return render(request, 'event/event.html')