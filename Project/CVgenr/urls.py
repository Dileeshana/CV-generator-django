from django.urls import path
from . import views

app_name = "CVpages"

urlpatterns = [
    path('button/', views.button, name="button"),

    path('ogcreatehtml/', views.ogcreatehtml, name="ogcreatehtml"),
    path('update_Cv/<str:pk>/', views.updatecv, name="update_cv"),

]



