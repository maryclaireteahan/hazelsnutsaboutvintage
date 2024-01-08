from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_events, name='events'),
    path('<slug:slug>/', views.event_detail, name='single_event'),
    path('add/', views.add_event, name='add_event'),
    path('edit/<slug:slug>/', views.event_edit, name='edit_event'),
    path('delete/<slug:slug>/', views.delete_event, name='delete_event'),
    
]
