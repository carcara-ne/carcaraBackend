from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")

def scatter(request):
    return HttpResponse("Scatter")

def pie(request):
    return HttpResponse("Pie")

def column(request):
    return HttpResponse("Column")
