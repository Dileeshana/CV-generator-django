from email.headerregistry import Address
from email.policy import default
from tabnanny import verbose
from unicodedata import name
from django.db import models

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


#all models here.

class Cvdetails(models.Model):

    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    your_title = models.CharField(max_length=500, blank=True, null=True)
    nic = models.CharField(max_length=20, null=True)
    # avatar = models.ImageField(null=True, default=n)
    date_of_birth = models.DateField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    mobile_contact = models.CharField(max_length=10, null=True)
    home_contact = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=100, null=True)
    experience = models.TextField(null=True)
    skill1 = models.CharField(max_length=50, null=True)
    skill2 = models.CharField(max_length=50, null=True)
    skill3 = models.CharField(max_length=50, null=True)
    skill4 = models.CharField(max_length=50, null=True)
    skill5 = models.CharField(max_length=50, null=True)
    skill6 = models.CharField(max_length=50, null=True)
    education = models.TextField(null=True)
    # ol_result = models.CharField(max_length=100, null=True)
    # al_stream = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name

