from django.shortcuts import render
import logging
import utils

logger = logging.getLogger(__name__)

def index(request):
    context = {}
    return render(request, 'homeful/index.html', context)

def list(request):
    context = {}
    return render(request, 'homeful/content1.html', context)
