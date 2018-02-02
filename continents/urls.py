from django.urls import path
from . import views

app_name = 'continents'

urlpatterns = [
    path('', views.ContinentsView.as_view(), name="continents")
]