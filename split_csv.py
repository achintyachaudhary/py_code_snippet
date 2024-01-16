import csv
import os


def split_csv(input_csv, output_folder, num_files):
    with open(input_csv, 'r') as infile:
        reader = csv.reader(infile)
        header = next(reader)

        # Calculate the number of rows per file
        total_rows = sum(1 for row in reader)
        rows_per_file = total_rows // num_files

        # Reset the file pointer to the beginning of the file
        infile.seek(0)
        next(reader)  # Skip header

        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Write rows to each file
        for i in range(num_files):
            output_file = os.path.join(output_folder, f'output_file_{i + 1}.csv')
            with open(output_file, 'w', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(header)
                for _ in range(rows_per_file):
                    try:
                        row = next(reader)
                        writer.writerow(row)
                    except StopIteration:
                        break


# Example usage
input_csv_file = '/Users/archaudhary/Documents/projects/py_snippets/all_india_PO_list.csv'
output_folder = 'spliteed_input'
num_files = 30

split_csv(input_csv_file, output_folder, num_files)
