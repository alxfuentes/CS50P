from validator_collection import validators, errors

def main():
    email = input("Email: ")
    if validate_email(email):
        print("Valid")
    else:
        print("Invalid")

def validate_email(email):
    # Placeholder for email validation logic
    try:
        validators.email(email)
        return True
    except errors.InvalidEmailError:
        return False

if __name__ == "__main__":
    main()