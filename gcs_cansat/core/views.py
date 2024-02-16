from django.shortcuts import render
from .graphs import processing, main_plot_data,map_plot_data,display_data

def display(request):

    context = display_data()
    return render(request,'core/display.html',context)

def main_plot(request):

    context = main_plot_data()
    return render(request, 'core/main_plot.html', context)

def map_plot(request):

    context = map_plot_data()
    return render(request,'core/map_plot.html',context)
    




