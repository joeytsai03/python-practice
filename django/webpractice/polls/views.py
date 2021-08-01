from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    request.method
    return HttpResponse("Hello, world. You're at the polls index.")
