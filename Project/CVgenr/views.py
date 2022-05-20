from multiprocessing import context
from django.template import RequestContext
#from operator import mod
#from pyexpat import model
#from re import template
from django.shortcuts import render, redirect
from django.http import HttpResponse

#from django.views import generic
from django.contrib import messages
from .models import * 
from .forms import CvDetailsForm

# def cvcreate(request):

#     form = CvDetailsForm()
#     if request.method == 'POST':
#         #print('',request.POST)
#         form = CvDetailsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/button')


#     context = {'form':form}
#     return render(request, 'CVpages/trial.html', context)


def readcvbtn(request):
    cvdata = Cvdetails.objects.all()

    return render(request, 'CVpages/dil_preBtn.html', {'cvdata': cvdata})



def ogcreatehtml(request):

    form = CvDetailsForm()
    if request.method == 'POST':
        #print('',request.POST)
        form = CvDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/button')

    context = {'form':form}
    return render(request, 'CVpages/dilcvcreate.html', context)


def updatecv(request, pk):

    cvdata = Cvdetails.objects.get(id=pk)
    form = CvDetailsForm(instance = cvdata)

    if request.method == 'POST':
        form = CvDetailsForm(request.POST, instance = cvdata)
        if form.is_valid():
            form.save()
            return redirect('/button')

    context = {'form':form}
    return render(request, 'CVpages/dilcvcreate.html', context)


def deleteCv(request, pk):
    cvdata = Cvdetails.objects.get(id=pk)

    if request.method == 'POST':
            cvdata.delete()
            return redirect('/button')


    context = {'form':cvdata}
    return render(request, 'CVpages/dilcvdiscard.html', context)


def portfoloio(request, pk):
    portfolio = Cvdetails.objects.get(id=pk)

    return render(request, 'CVpages/dil_portfolio.html', {'cvdata': portfolio})