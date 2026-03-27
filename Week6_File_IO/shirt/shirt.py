import sys
import os
from PIL import Image
from PIL import ImageOps

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments")

    filename = sys.argv[1]
    output_filename = sys.argv[2]

    fileext = os.path.splitext(filename)[1]
    output_fileext = os.path.splitext(output_filename)[1]

    #print(fileext)
    #print(output_fileext)

    if fileext != output_fileext:
        sys.exit("Input and output have different extensions")

    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    try:
        with Image.open(filename) as before:
            with Image.open("shirt.png") as shirt:
                size = shirt.size
                before = ImageOps.fit(before, size)
                before.paste(shirt, shirt)
                before.save(output_filename)
                # before.show()
            
    except Exception as e:
        sys.exit(f"Error on file access: {e}")

if __name__ == "__main__":
    main()