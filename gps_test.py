from geopy.geocoders import Nominatim
from geopy.exc import GeocoderServiceError

# Initialize Nominatim API with a more descriptive user agent
geolocator = Nominatim(user_agent="my_geopy_app")

# Latitude & Longitude input
Latitude = "39.684393"
Longitude = "-8.519500"

try:
    location = geolocator.reverse(Latitude + "," + Longitude)
    address = location.raw['address']

    # Traverse the data
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    code = address.get('country_code')
    zipcode = address.get('postcode')

    print('City : ', city)
    print('State : ', state)
    print('Country : ', country)
    print('Zip Code : ', zipcode)

except GeocoderServiceError as e:
    print("Error: ", e)
