from django.urls import path
from . import views

urlpatterns = [
    path('', views.event, name='event'),
    path('create/', views.EventCreate.as_view(), name='event_create'),
    path('edit/<int:id>/', views.eventEdit, name='event_edit'),
    path('delete/<int:id>/', views.eventDelete, name='event_delete'),
]
