import sys
import pyfiglet
import random


def main():
    # Check command-line arguments
    if len(sys.argv) == 1:
        # Zero arguments - use random font
        available_fonts = pyfiglet.FigletFont.getFonts()
        font = random.choice(available_fonts)
    elif len(sys.argv) == 3:
        # Two arguments
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid option")
        font = sys.argv[2]
    else:
        sys.exit("Invalid number of command-line arguments")

    # Prompt user for text
    text = input("Input: ")

    # Render text in chosen font
    try:
        f = pyfiglet.Figlet(font=font)
        print(f.renderText(text))
    except pyfiglet.FontNotFound:
        sys.exit(f"Font not found: {font}")


if __name__ == "__main__":
    main()
