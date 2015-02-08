from django.db import models
import requests
import json

SEATTLE_FAIR_MARKET_RENTS_URL = 'http://services.arcgis.com/VTyQ9soqVukalItT/arcgis/rest/services/FairMarketRents/FeatureServer/0/query?where=&objectIds=&time=&geometry=%7B%22xmin%22%3A-13721209.831341939%2C%22ymin%22%3A6018679.182711435%2C%22xmax%22%3A-13514676.980915314%2C%22ymax%22%3A6064541.399682558%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%7D%7D&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Meter&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&quantizationParameters=&f=pjson&token='
SEATTLE_MULTI_FAMILY_PROPERTIES = 'http://services.arcgis.com/VTyQ9soqVukalItT/arcgis/rest/services/MultiFamilyProperties/FeatureServer/0/query?where=&objectIds=&time=&geometry=%7B%22xmin%22%3A-13721209.831341939%2C%22ymin%22%3A6018679.182711435%2C%22xmax%22%3A-13514676.980915314%2C%22ymax%22%3A6064541.399682558%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%7D%7D&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Meter&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&quantizationParameters=&f=pjson&token='

class FairMarketRent(models.Model):
    area_name = models.CharField(max_length=30)
    number_of_studios = models.IntegerField()
    number_of_1bedrooms = models.IntegerField()
    number_of_2bedrooms = models.IntegerField()
    number_of_3bedrooms = models.IntegerField()
    number_of_4bedrooms = models.IntegerField()

def populateSeattleFairMarketRents():
    list_of_fair_market_rents = requests.get(SEATTLE_FAIR_MARKET_RENTS_URL).json().get(u'features')
    for fair_market_rents in list_of_fair_market_rents:
        fair_market_rent_data = fair_market_rents.get(u'attributes')
        
        fair_market_rent_data.get(u'FMR_0BDR')
        fair_market_rent_data.get(u'FMR_1BDR')
        fair_market_rent_data.get(u'FMR_2BDR')
        fair_market_rent_data.get(u'FMR_3BDR')
        fair_market_rent_data.get(u'FMR_4BDR')
        fair_market_rent_data.get(u'FMR_AREANAME')

class MultiFamilyProperty(models.Model):
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=30)
    latitude = models.FloatField
    longitude = models.FloatField
    property_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)

def populateSeattleMultiFamilyProperties():
    list_of_multi_family_properties = requests.get(SEATTLE_MULTI_FAMILY_PROPERTIES).json().get(u'features')
    for multi_family_property in list_of_multi_family_properties:
        multi_family_property_data = multi_family_property.get(u'attributes')
        
        multi_family_property_data.get('STD_ADDR')
        multi_family_property_data.get('STD_CITY')
        multi_family_property_data.get('STD_ST')
        multi_family_property_data.get('STD_ZIP5')
        multi_family_property_data.get('LAT')
        multi_family_property_data.get('LON')
        multi_family_property_data.get('PROPERTY_NAME_TEXT')
        multi_family_property_data.get('PROPERTY_ON_SITE_PHONE_NUMBER')
