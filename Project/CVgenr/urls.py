from django.urls import path
from . import views

app_name = "CVpages"

urlpatterns = [
    path('button/', views.button, name="button"),
    path('ogcreatehtml/', views.ogcreatehtml, name="ogcreatehtml"),
    path('update_cv/<str:pk>/', views.updatecv, name="update_cv"),
    path('delete_cv/<str:pk>/', views.deleteCv, name="delete_cv"),

]



