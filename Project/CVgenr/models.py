from email.headerregistry import Address
from email.policy import default
from tabnanny import verbose
from unicodedata import name
from django.db import models

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


# Create your models here.

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

# class Skill(models.Model):
#     class Meta:
#         verbose_name_plural = 'Skills'
#         verbose_name = 'Skill'
    
#     name = models.CharField(max_length=20, blank=True, null=True)
#     score = models.IntegerField(default=80, blank=True, null=True)
#     image = models.FileField(blank=True, null=True, upload_to="skills")
#     is_key_skill = models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.name

# class UserProfile(models.Model):

#     class Meta:
#         verbose_name_plural = 'User Profiles'
#         verbose_name = 'User Profile'
    
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
#     title = models.CharField(max_length=200, blank=True, null=True)
#     bio = models.TextField(blank=True, null=True)
#     skills = models.ManyToManyField(Skill, blank=True)
#     cv = models.FileField(blank=True, null=True, upload_to="cv")

#     def __str__(self):
#         return f'{self.user.first_name} {self.user.last_name}'

# class Media(models.Model):

#     class Meta:
#         verbose_name_plural = 'Media Files'
#         verbose_name = 'Media'
#         ordering = ["name"]
	
#     image = models.ImageField(blank=True, null=True, upload_to="media")
#     url = models.URLField(blank=True, null=True)
#     name = models.CharField(max_length=200, blank=True, null=True)
#     is_image = models.BooleanField(default=True)

#     def save(self, *args, **kwargs):
#         if self.url:
#             self.is_image = False
#         super(Media, self).save(*args, **kwargs)
#     def __str__(self):
#         return self.name

# class Portfolio(models.Model):

#     class Meta:
#         verbose_name_plural = 'Portfolio Profiles'
#         verbose_name = 'Portfolio'
#         ordering = ["name"]
#     date = models.DateTimeField(blank=True, null=True)
#     name = models.CharField(max_length=200, blank=True, null=True)
#     description = models.CharField(max_length=500, blank=True, null=True)
#     body = RichTextField(blank=True, null=True)
#     image = models.ImageField(blank=True, null=True, upload_to="portfolio")
#     slug = models.SlugField(null=True, blank=True)
#     is_active = models.BooleanField(default=True)

#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.slug = slugify(self.name)
#         super(Portfolio, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return f"/portfolio/{self.slug}"