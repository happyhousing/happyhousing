from django.shortcuts import render
import logging
from homeful.hud_helper import getSeattleFairMarketRents, getSeattleMultiFamilyProperties

logger = logging.getLogger(__name__)

def index(request):
    context = {}
    return render(request, 'homeful/index.html', context)

def list(request):
    zipcode = request.GET['zipcode']
    rooms = request.GET['rooms']
    price = request.GET['price']
    context = {}
    
    fmrs = getSeattleFairMarketRents()
    mfps = getSeattleMultiFamilyProperties()
    
    # modify FMRs and MFPs based on request HERE
    
    context['fmrs'] = fmrs
    context['mfps'] = mfps
    
    return render(request, 'homeful/content1.html', context)
