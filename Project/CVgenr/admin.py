from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Cvdetails)
admin.site.register(Skill)
admin.site.register(UserProfile)
admin.site.register(Media)
admin.site.register(Portfolio)