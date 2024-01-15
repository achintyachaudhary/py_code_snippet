from geopy.geocoders import Nominatim


def get_lat_long_from_pincode(pincode):
    geolocator = Nominatim(user_agent="geo_locator")

    try:
        location = geolocator.geocode(pincode)
        if location:
            latitude, longitude = location.latitude, location.longitude
            return latitude, longitude
        else:
            print(f"Location not found for pincode: {pincode}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None


# Example usage
pincode = "208024"  # Replace with the desired pincode
result = get_lat_long_from_pincode(pincode)

if result:
    latitude, longitude = result
    print(f"Latitude: {latitude}, Longitude: {longitude}")
