from django.shortcuts import HttpResponse,render
from django.shortcuts import render

# Create your views here.


def Index(request):
    return HttpResponse(":))")