
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_events, name='events'),
    path('add/', views.add_event, name='add_event'),
    path('<slug:slug>/', views.single_event, name='single_event'),
    path('edit/<slug:slug>/', views.edit_event, name='edit_event'),
    path('delete/<slug:slug>/', views.delete_event, name='delete_event'),
]
