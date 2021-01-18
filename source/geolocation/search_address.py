from geopy.geocoders import Nominatim
from . import forms


def searchAddress(field_form):
    form = forms.FormAddress
    field_form = form.base_fields['address'].label
    geolocator = Nominatim(user_agent="Geolocation")
    location = geolocator.geocode(field_form)
    return location
    #print((location.latitude, location.latitude))
    #print(location.raw)