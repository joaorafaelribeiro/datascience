from geopy.geocoders import Nominatim

def location(cep):
    geolocator = Nominatim(user_agent="geolocalização")
    return geolocator.geocode(cep,timeout=1) 
 
 