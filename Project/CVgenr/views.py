from multiprocessing import context
from operator import mod
from pyexpat import model
from re import template
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views import generic
from django.contrib import messages
from .models import * 
from .forms import CvDetailsForm

def cvcreate(request):

    form = CvDetailsForm()
    if request.method == 'POST':
        #print('',request.POST)
        form = CvDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('button')


    context = {'form':form}
    return render(request, 'CVpages/trial.html', context)


def button(request):
    return render(request, 'CVpages/dil_preButtons.html')



class IndexView(generic.TemplateView):
    template= "CVpages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        portfolio = Portfolio.objects.filter(is_active=True)

        context["portfolio"] = portfolio
        return context

class PortfolioView(generic.ListView):
    model = Portfolio
    template = "CVpages/portfolio.html"
    paginate_by =10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class PortfolioDetailed(generic.DetailView):
    model = Portfolio
    template = "CVpages/portfolio-detail.html"
