from django.shortcuts import render
from .models import *

# Create your views here.

def helpcentre_home(request):
    #messages = NPS.objects.all()
    #sender = Theme_label.objects.all()
    #agent = Author.objects.all()

    #context = {
    #    'nps_items': nps_items,
    #    'themes': themes,
    #    'author': author,
    #}
    return render(request, 'helpcentre/index.html') 
