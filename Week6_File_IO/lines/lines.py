import sys
import os

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith('.py'):
        sys.exit("Not a Python file")

    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    try:
        with open(filename, 'r') as file:
            count = 0
            for line in file:
                stripped = line.strip()
                if stripped and not stripped.startswith('#'):
                    count += 1
            print(count)
    except Exception as e:
        sys.exit(f"Error reading file: {e}")

if __name__ == "__main__":
    main()
    