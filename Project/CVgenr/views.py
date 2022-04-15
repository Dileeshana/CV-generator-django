from django.shortcuts import render
from django.http import HttpResponse

def cvcreate(request):
    return render(request, 'CVpages/dilcvcreate.html')


