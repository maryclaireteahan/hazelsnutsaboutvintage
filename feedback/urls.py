from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.all_feedback, name='all_feedback'),
    path('feedback/<int:feedback_id>/',
         views.feedback_detail, name='feedback_detail'),
]
