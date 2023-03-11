from django.shortcuts import render
from django.http import HttpResponse

def koti(request):
    return HttpResponse('<marquee><h1 style="color:blue">koti is best all rounder<h1></marquee>')

# Create your views here.
