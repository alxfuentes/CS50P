import sys
import os
import csv

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments")

    filename = sys.argv[1]
    output_filename = sys.argv[2]

    if not filename.endswith('.csv'):
        sys.exit("Not a CSV file")

    if not output_filename.endswith('.csv'):
        sys.exit("Output file is not a CSV file")

    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            with open(output_filename, 'w', newline='') as output_file:
                writer = csv.writer(output_file)
                writer.writerow(['first', 'last', 'house'])       
                for row in reader:
                    name_parts = row['name'].split(', ')
                    first_name = name_parts[1]
                    last_name = name_parts[0]
                    writer.writerow([first_name, last_name, row['house']])
            
    except Exception as e:
        sys.exit(f"Error on file access: {e}")

if __name__ == "__main__":
    main()