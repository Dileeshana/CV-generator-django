import imp
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
from .filters import *

from django.template.loader import get_template
from xhtml2pdf import pisa

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

    cvfilter = CvFilter(request.GET, queryset=cvdata)
    cvdata = cvfilter.qs

    return render(request, 'CVpages/dil_preBtn.html', {'cvdata': cvdata , 'cvfilter':cvfilter })



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

    return render(request, 'CVpages/pdf1.html', {'cvdata': portfolio})


def render_pdf_view(request, pk):

    cvdata = Cvdetails.objects.get(id=pk)
    template_path = 'CVpages/pdf2.html'
    context = {'cvdata': cvdata }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download:
    response['Content-Disposition'] = 'attachment; filename="Resume.pdf"'
    # if display:
    # response['Content-Disposition'] = 'filename="Resume.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
