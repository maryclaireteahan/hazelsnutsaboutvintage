from django.urls import path
from . import views

urlpatterns = [
    path('', views.coupon, name='coupon'),
    path('generate_coupon/<order_number>/', views.generate_coupon, name='generate_coupon'),
]
