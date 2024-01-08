from django.urls import path 
from eventapp import views

urlpatterns = [
    path('' , views.home  , name='home'),
    path('event/', views.event , name='event'),
    path('register/', views.RegistrationForm , name='RegistrationForm'),
    path('eventD/<event_id>', views.event_detail , name='event_detail')
]
