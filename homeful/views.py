from django.shortcuts import render
import logging
from homeful.hud_helper import getSeattleFairMarketRents, getSeattleMultiFamilyProperties

logger = logging.getLogger(__name__)

def index(request):
    context = {}
    return render(request, 'homeful/index.html', context)

def help(request):
    context = {}
    return render(request, 'homeful/help.html', context)

def list(request):
    zipcode = request.GET['zipcode']
    rooms = request.GET['rooms']
    #price = request.GET['price']
    context = {}
    
    fmrs = getSeattleFairMarketRents()
    mfps = getSeattleMultiFamilyProperties()
    
    # modify FMRs and MFPs based on request HERE
    
    seattle_fmr = dict()
    for fmr in fmrs:
        if fmr['area'] == u'Seattle-Bellevue, WA HUD Metro FMR Area':
            seattle_fmr = fmr
    
    mfps = filterByZipcode(zipcode, mfps)
    
    context['mfps'] = mfps
    context['rooms'] = rooms
    context['zipcode'] = zipcode
    
    estimated_price = seattle_fmr[rooms + 'br']
    price_range_max = estimated_price + (estimated_price*.12)
    price_range_min = estimated_price - (estimated_price*.12)
    context['price_range'] = "$" + "{0:.2f}".format(price_range_min) + " - $" + "{0:.2f}".format(price_range_max)
    
    return render(request, 'homeful/content1.html', context)

def filterByZipcode(zipcode, mfps):
    def myfilter(mfp):
        return mfp['zipcode'] == zipcode
    return filter(myfilter, mfps)
