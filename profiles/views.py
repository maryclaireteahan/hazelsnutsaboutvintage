from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm

def profile(request):
    """ A view to return the profile page """
    profile = get_object_or_404(UserProfile, user=request.user)
    
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }
    
    return render(request, 'profiles/profile.html')