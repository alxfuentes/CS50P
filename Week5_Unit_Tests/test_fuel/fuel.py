def main():
    data = input("Fraction: ")
    indicate = convert(data)
    print(gauge(indicate))

def convert(fraction):
    try:
        x, y = map(int, fraction.split('/'))
    except ValueError:
        raise ValueError("Invalid fraction format")

    if x > y:
        raise ValueError("Numerator cannot be greater than denominator")
    if y == 0:
        raise ValueError("Denominator cannot be zero")
    return round(x / y, 2) * 100

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{int(percentage)}%"
    
if __name__ == "__main__":
    main()
    