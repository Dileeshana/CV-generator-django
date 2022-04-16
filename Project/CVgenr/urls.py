from django.urls import path
from . import views

urlpatterns = [
    path('cvcreate/', views.cvcreate, name="cv_create"),
    path('button/', views.button, name="button"),
]



