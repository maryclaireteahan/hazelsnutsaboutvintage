from multiprocessing import context
from re import template
from django.shortcuts import render

def profile(request):
    """ A view to return the profile page """
    
    template = 'profiles/profile.html'
    context = {}
    
    return render(request, 'profiles/profile.html')