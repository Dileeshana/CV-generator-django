from django.urls import path
from . import views

app_name = "CVpages"

urlpatterns = [
    # path('cvcreate/', views.cvcreate, name="cv_create"),
    path('button/', views.button, name="button"),

    path('ogcreatehtml/', views.ogcreatehtml, name="ogcreatehtml"),

    # path('index/', views.IndexView.as_view(), name="index_view"),
    # path('portfolio/', views.PortfolioView.as_view(), name="portfolio_view"),
    # path('portfolio/<slug:slug>', views.PortfolioDetailed.as_view(), name="portfolio_detailed"),
]



