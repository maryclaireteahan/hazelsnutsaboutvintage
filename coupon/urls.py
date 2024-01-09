from django.urls import path
from . import views

urlpatterns = [
    path('coupon/<str:coupon_code>/', views.coupon, name='coupon'),
]
