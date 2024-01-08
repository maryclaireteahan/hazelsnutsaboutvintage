from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback, name='feedback'),  
    path('<int:feedback_id>/', views.feedback_detail, name='feedback_detail'),
]