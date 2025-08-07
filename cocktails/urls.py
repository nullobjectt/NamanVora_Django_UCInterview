# searchbar/urls.py
from django.urls import path
from .views import search_cocktails

urlpatterns = [
    path('search/', search_cocktails, name='search_cocktails'),
]
