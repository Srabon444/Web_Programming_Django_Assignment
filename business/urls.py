from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='business-home'),
    path('home/', views.home, name='business-home'),
    path('payment/', views.payment, name='business-payment'),
    path('login/', views.login, name='business-login'),
]
