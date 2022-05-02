from django.urls import path
from . import views

urlpatterns = [
    path('cvcreate/', views.cvcreate, name="cv_create"),
    path('button/', views.button, name="button"),

    path('index/', views.IndexView.as_view(), name="index_view"),
    path('portfolio/', views.PortfolioView.as_view(), name="portfolio_view"),
    path('portfolio/<slug:slug>', views.PortfolioDetailed.as_view(), name="portfolio_detailed"),
]



