from django.urls import path
from . import views as core_views

urlpatterns=[
    path('plot/', core_views.plot, name = 'plot'),
    path('',core_views.toggle, name = 'toggle'),
]