from django.urls import path
from . import views

app_name = "CVpages"

urlpatterns = [
    path('button/', views.readcvbtn, name="button"),
    path('ogcreatehtml/', views.ogcreatehtml, name="ogcreatehtml"),
    path('updatecv/<str:pk>/', views.updatecv, name="updatecv"),
    path('deletecv/<str:pk>/', views.deleteCv, name="deletecv"),
    path('portfoloio/<str:pk>/', views.portfoloio, name="portfoloio"),

]



