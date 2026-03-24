import sys
import os
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith('.csv'):
        sys.exit("Not a CSV file")

    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
            print(tabulate(data, headers="firstrow", tablefmt="grid"))
            
    except Exception as e:
        sys.exit(f"Error reading file: {e}")

if __name__ == "__main__":
    main()