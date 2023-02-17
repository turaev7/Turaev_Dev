from django.shortcuts import render

from .models import Me
from django.views.generic import ListView

class MeView(ListView):
    model = Me
    context_object_name="Info"
    template_name= "blog/index.html"