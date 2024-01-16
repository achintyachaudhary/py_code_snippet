import csv
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


def update_csv_with_lat_long(input_csv, output_csv):
    iterator = 0
    with open(input_csv, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['latitude', 'longitude']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            print(iterator)
            iterator += 1
            pincode = row['pincode']
            lat_long = get_lat_long_from_pincode(pincode)
            if lat_long:
                row['latitude'], row['longitude'] = lat_long
                writer.writerow(row)
            else:
                # If location is not found, still write the original row
                writer.writerow(row)


# Example usage
input_csv_file = '/Users/archaudhary/Documents/projects/py_snippets/all_india_PO_list.csv'
output_csv_file = 'output_file_with_lat_long.csv'

update_csv_with_lat_long(input_csv_file, output_csv_file)
