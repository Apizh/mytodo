from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home(request: HttpRequest):
    return HttpResponse("'message': 'Welcome to our website!'")