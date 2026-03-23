def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def valid_length(s):
    if len(s) < 2 or len(s) > 6:
        return False
    else:
        return True

def valid_start(s):
    if( s[0].isalpha() and s[1].isalpha() ):
        return True
    else:
        return False

def valid_characters(s):
    for c in s:
        if not c.isalpha() and not c.isdigit():
            return False
    return True

def has_digits(s):
    for c in s:
        if c.isdigit():
            return True
    return False

def valid_digits(s):
    hasdigits = False
    lastdigit = False

    for c in s:
        if c.isdigit():
            if c == '0' and not hasdigits:
                return False
            hasdigits = True
            lastdigit = True

        if c.isalpha() and hasdigits:
            return False
    return lastdigit

def is_valid(s):
    valid = False
    valid = valid_length(s)
    valid = valid and valid_start(s)
    valid = valid and valid_characters(s)
    if has_digits(s):
        valid = valid and valid_digits(s)
    return valid

if __name__ == "__main__":
    main()
