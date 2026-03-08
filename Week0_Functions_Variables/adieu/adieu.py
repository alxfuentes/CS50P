def main():
    names = []
    
    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        print()
    
    # Format and output the farewell message
    if len(names) == 1:
        print(f"Adieu to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu to {names[0]} and {names[1]}")
    else:
        # Format: "Adieu to name1, name2, and name3"
        print(f"Adieu to {', '.join(names[:-1])}, and {names[-1]}")


if __name__ == "__main__":
    main()
