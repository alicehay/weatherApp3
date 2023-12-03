from datetime import (datetime)

import geocoder
import requests
from django.http import HttpResponse
# installed package requests
from django.template import loader
from myweather.models import Worldcities


def temp_somewhere(request):
    random_item = Worldcities.objects.all().order_by('?').first()
    city = random_item.city
    location = [random_item.lat, random_item.lng]
    temp = get_temp(location)

    template = loader.get_template('index.html')
    # index name of html file
    context = {
        'city': city,
        'temp': temp}
    # dictionary of values
    # want to return template of text
    return HttpResponse(template.render(context, request))

def temp_current(request):
    # geocoder - python library
    current_location = geocoder.ip('me').latlng
    temp = get_temp(current_location)

    template = loader.get_template('index.html')
    # index name of html file
    context =  {
        'city' : 'Your Location',
        'temp' : temp}
    # dictionary of values
    # want to return template of text
    return HttpResponse(template.render(context, request))


def get_temp(current_location):
    # weather forcast API
    endpoint = "https://api.open-meteo.com/v1/forecast"
    # grab 1st,2nd item on location
    api_request = f"{endpoint}?latitude={current_location[0]}&longitude={current_location[1]}&hourly=temperature_2m"
    # convert to json form (transfer data as text that can be sent over a network)
    now = datetime.now()
    current_hour = now.hour
    meteo_data = requests.get(api_request).json()
    temp = meteo_data['hourly']['temperature_2m'][current_hour]
    return temp

def make_list(request):
    new_zealand_cities = Worldcities.objects.filter(country='New Zealand')
    template = loader.get_template('city_list.html')
    context = {
        'cities': new_zealand_cities
    }
    return HttpResponse(template.render(context, request))