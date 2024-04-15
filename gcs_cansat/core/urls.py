from django.urls import path
from . import views as core_views

urlpatterns=[
    path('',core_views.display, name = 'display'),
    path('plot/', core_views.main_plot, name = 'main-plot'),
    path('main-api/',core_views. main_API,name = 'main-api'),
    path('map-plot/',core_views.map_plot,name = 'map-plot'),
]