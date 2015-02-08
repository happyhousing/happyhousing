import requests
import json

SEATTLE_FAIR_MARKET_RENTS_URL = 'http://services.arcgis.com/VTyQ9soqVukalItT/arcgis/rest/services/FairMarketRents/FeatureServer/0/query?where=&objectIds=&time=&geometry=%7B%22xmin%22%3A-13721209.831341939%2C%22ymin%22%3A6018679.182711435%2C%22xmax%22%3A-13514676.980915314%2C%22ymax%22%3A6064541.399682558%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%7D%7D&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Meter&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&quantizationParameters=&f=pjson&token='
SEATTLE_MULTI_FAMILY_PROPERTIES = 'http://services.arcgis.com/VTyQ9soqVukalItT/arcgis/rest/services/MultiFamilyProperties/FeatureServer/0/query?where=&objectIds=&time=&geometry=%7B%22xmin%22%3A-13721209.831341939%2C%22ymin%22%3A6018679.182711435%2C%22xmax%22%3A-13514676.980915314%2C%22ymax%22%3A6064541.399682558%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%7D%7D&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Meter&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&quantizationParameters=&f=pjson&token='

def populateSeattleFairMarketRents():
    list_of_fair_market_rents = requests.get(SEATTLE_FAIR_MARKET_RENTS_URL).json().get(u'features')
    fmrs = list()
    for fair_market_rents in list_of_fair_market_rents:
        fair_market_rent_data = fair_market_rents.get(u'attributes')
        
        fmr = dict()
        fmr['0br'] = fair_market_rent_data.get(u'FMR_0BDR')
        fmr['1br'] = fair_market_rent_data.get(u'FMR_1BDR')
        fmr['2br'] = fair_market_rent_data.get(u'FMR_2BDR')
        fmr['3br'] = fair_market_rent_data.get(u'FMR_3BDR')
        fmr['4br'] = fair_market_rent_data.get(u'FMR_4BDR')
        fmr['area'] = fair_market_rent_data.get(u'FMR_AREANAME')
        
        fmrs.append(fmr)
    return fmrs

def populateSeattleMultiFamilyProperties():
    list_of_multi_family_properties = requests.get(SEATTLE_MULTI_FAMILY_PROPERTIES).json().get(u'features')
    mfps = list()
    for multi_family_property in list_of_multi_family_properties:
        multi_family_property_data = multi_family_property.get(u'attributes')
        
        mfp = dict()
        mfp['address'] = multi_family_property_data.get('STD_ADDR')
        mfp['city'] = multi_family_property_data.get('STD_CITY')
        mfp['state'] = multi_family_property_data.get('STD_ST')
        mfp['zipcode'] = multi_family_property_data.get('STD_ZIP5')
        mfp['latitude'] = multi_family_property_data.get('LAT')
        mfp['longitude'] = multi_family_property_data.get('LON')
        mfp['name'] = multi_family_property_data.get('PROPERTY_NAME_TEXT')
        mfp['phone'] = multi_family_property_data.get('PROPERTY_ON_SITE_PHONE_NUMBER')
        
        mfps.append(mfp)
    return mfps
