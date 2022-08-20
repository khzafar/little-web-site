from django.shortcuts import render
from django.views.generic import ListView
from .models import News

class HomePageView(ListView):
    model = News
    template_name = 'home.html'
    
