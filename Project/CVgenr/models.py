from email.headerregistry import Address
from unicodedata import name
from django.db import models

# Create your models here.

class Cvdetails(models.Model):

    SUBJECTS = (
        ('Com Maths','Com Maths'),
        ('chem','chem'),
        ('P6','P6'),
    )

    name = models.CharField(max_length=100, null=True)
    dob = models.DateField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    mobile_contact = models.CharField(max_length=10, null=True)
    home_contact = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=100, null=True)
    postalcode = models.CharField(max_length=10, null=True)
    project = models.CharField(max_length=100, null=True)
    certificate = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=100, null=True)
    volunteering = models.CharField(max_length=100, null=True)
    ol_result = models.CharField(max_length=100, null=True)
    al_stream = models.CharField(max_length=100, null=True)
    subject1 = models.CharField(max_length=100, null=True, choices=SUBJECTS)
    subject2 = models.CharField(max_length=100, null=True, choices=SUBJECTS)
    subject3 = models.CharField(max_length=100, null=True, choices=SUBJECTS)
    skill = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name
