import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^([0-9]{1,2})(?::([0-9]{2}))? (AM|PM) to ([0-9]{1,2})(?::([0-9]{2}))? (AM|PM)$"
    match = re.search(pattern, s)
    if not match:
        raise ValueError("Invalid time format")

    start_hour = int(match.group(1))
    start_minute = match.group(2)
    start_period = match.group(3)
    end_hour = int(match.group(4))
    end_minute = match.group(5)
    end_period = match.group(6)

    if start_minute is None:
        start_minute = 0
    else:
        start_minute = int(start_minute)

    if end_minute is None:
        end_minute = 0
    else:
        end_minute = int(end_minute)

    if not 1 <= start_hour <= 12 or not 0 <= start_minute <= 59:
        raise ValueError("Invalid time")
    if not 1 <= end_hour <= 12 or not 0 <= end_minute <= 59:
        raise ValueError("Invalid time")

    def to_24(hour, minute, period):
        if period == "AM":
            if hour == 12:
                hour = 0
        else:
            if hour != 12:
                hour += 12
        return f"{hour:02d}:{minute:02d}"

    start_24 = to_24(start_hour, start_minute, start_period)
    end_24 = to_24(end_hour, end_minute, end_period)

    return f"{start_24} to {end_24}"

if __name__ == "__main__":
    main()
