from geopy.geocoders import Nominatim

def location(cep):
 geolocator = Nominatim(user_agent="geolocalização")
 location = geolocator.geocode(cep)
 if location:
     return (location.latitude, location.longitude)
 return None
 