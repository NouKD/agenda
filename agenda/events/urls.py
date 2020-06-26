from django.urls import path
from . import views

urlpatterns = [
    path('events', views.events, name='events'),
    path('single_event', views.single_event, name='single_event'),
    path('event_N', views.event_N, name='event_N'),
]