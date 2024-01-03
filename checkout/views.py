from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    """ A view to return the checkout page """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OMXraKxtCs4iFlaWGQfH54kPhgbdQZxa7f3VBOL1mJ9uW3Bd0w0yW9jrvr5QHhIcjo9qtcxh381T8ofe90NrYtx001vmn5dXN',
        'client_secret': 'test client secret',
    }
    
    return render(request, template, context)