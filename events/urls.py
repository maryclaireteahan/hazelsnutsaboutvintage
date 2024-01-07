from django.urls import path
from . import views

urlpatterns = [
    path('', views.Events.as_view(), name='events'),
    path('<slug:slug>/', views.EventDetail.as_view(), name='single_event'),
    path('<slug:slug>/edit/', views.EventEdit.as_view(), name='edit_event'),
]
