from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import * 
from .forms import CvDetailsForm

def cvcreate(request):

    form = CvDetailsForm()
    if request.method == 'POST':
        #print('',request.POST)
        form = CvDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form':form}
    return render(request, 'CVpages/trial.html', context)


