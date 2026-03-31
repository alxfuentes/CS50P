import re

def main():
    print(count(input("Text: ")))


def count(s):
    # Find all occurrences of "um" as a whole word, case-insensitive
    # Excludes words that start with, contain, or end with "um" (only counts standalone "um")
    um_words = re.findall(r'\bum\b', s, re.IGNORECASE)
    return len(um_words)

if __name__ == "__main__":
    main()
    
    