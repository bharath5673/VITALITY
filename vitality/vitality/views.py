from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request, 'base.html')

def agency(request):
    return render(request, 'agency.html')

def culinary(request):
    return render(request, 'culinary.html')

def fashion(request):
    return render(request, 'fashion.html')

def video(request):
    return render(request, 'video.html')

def creative(request):
    return render(request, 'creative.html')

def legal(request):
    return render(request, 'legal.html')

def index(request):
    return render(request, 'static/docs/index.html')
