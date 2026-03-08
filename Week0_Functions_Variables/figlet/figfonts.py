from pyfiglet import Figlet

figlet = Figlet()

fonts = figlet.getFonts()

for font in fonts:
    print(font)
