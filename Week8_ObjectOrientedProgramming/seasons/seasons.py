import sys
import inflect
from datetime import date

def main():
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    try:
        birthdate = date.fromisoformat(birthdate)
    except ValueError:
        sys.exit("Invalid date format. Please use YYYY-MM-DD.")

    minutes = minutes_passed(birthdate) 
    print(f"You have been alive for {minutes} minutes.")
    print(to_words(minutes))

def minutes_passed( birthdate ) -> int:
    today = date.today()
    age = today - birthdate
    return age.days * 24 * 60

def to_words( number ) -> str:
    p = inflect.engine()
    return p.number_to_words(number, andword="")

if __name__ == "__main__":
    main()