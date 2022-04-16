from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Cvdetails

class CvDetailsForm(ModelForm):
    class Meta:
        model = Cvdetails
        fields = '__all__'