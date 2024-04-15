from django.shortcuts import render
from .graphs import processing, main_plot_data,display_data,new_map
from django.http import JsonResponse

def display(request):

    context = display_data()
    return render(request,'core/base.html',context)

def main_plot(request):

    context = main_plot_data()
    return render(request, 'core/main_plot.html', context)

def main_API(request):

    context = main_plot_data()
    return JsonResponse(context)

# def map_plot(request):
    
#     context = main_plot_data()
#     return render(request, 'core/map_plot.html', context)
  
def map_plot(request):
    new_map()
    return render(request,'core/map.html')





