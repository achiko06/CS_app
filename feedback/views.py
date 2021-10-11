from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    nps_items = NPS.objects.all()
    themes = Theme_label.objects.all()
    author = Author.objects.all()

    context = {
        'nps_items': nps_items,
        'themes': themes,
        'author': author,
    }
    return render(request, 'feedback/index.html', context)
