import re

def validate(ip):
    # Regex pattern for valid IPv4 address without leading zeros
    pattern = r'^(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$'
    return bool(re.match(pattern, ip))

def main():
    ip = input("IPv4 Address: ")
    if validate(ip):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
    