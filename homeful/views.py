from django.shortcuts import render
import logging
import utils

logger = logging.getLogger(__name__)

def index(request):
    context = {}
    return render(request, 'homeful/index.html', context)

def test(request):
    context = {}
    return render(request, 'homeful/test.html', context)
