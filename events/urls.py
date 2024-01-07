# from django.urls import path
# from . import views

# app_name = 'events'

# urlpatterns = [
#     path('', views.Events.as_view(), name='events'),
#     path('<slug:slug>/', views.EventDetail.as_view(), name='single_event'),
#     path('edit_event/<slug:slug>/', views.EventEdit.as_view(), name='edit_event'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_events, name='events'),
    path('<slug:slug>/', views.event_detail, name='single_event'),
    path('add/', views.add_event, name='add_event'),
    path('edit/<slug:slug>/', views.edit_event, name='edit_event'),
    path('delete/<slug:slug>/', views.delete_event, name='delete_event'),
    
]
