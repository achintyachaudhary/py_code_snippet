import csv
from geopy.geocoders import Nominatim
from concurrent.futures import ProcessPoolExecutor
import os

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

def process_file(input_file, output_file):
    print(f"Processing {input_file}...")
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['latitude', 'longitude']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            print("arlols")
            pincode = row['pincode']
            lat_long = get_lat_long_from_pincode(pincode)
            if lat_long:
                row['latitude'], row['longitude'] = lat_long
                writer.writerow(row)
            else:
                # If location is not found, still write the original row
                writer.writerow(row)

def update_csv_with_lat_long_in_parallel(input_folder, output_folder):
    input_files = ["/Users/archaudhary/Documents/projects/py_snippets/spliteed_input/output_file_2.csv"]
    output_files = [os.path.join(output_folder, f'output_{i}.csv') for i in range(len(input_files))]

    if __name__ == '__main__':
        from multiprocessing import freeze_support
        freeze_support()

        with ProcessPoolExecutor() as executor:
            executor.map(process_file, [os.path.join(input_folder, f) for f in input_files], output_files)

# Example usage
input_folder = '/Users/archaudhary/Documents/projects/py_snippets/spliteed_input'
output_folder = '/Users/archaudhary/Documents/projects/py_snippets/achintya/bb'

update_csv_with_lat_long_in_parallel(input_folder, output_folder)
