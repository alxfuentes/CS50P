import os

def main():
    main_menu()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main_menu():
    while True:
        clear_screen()
        print("Main Menu:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("You selected Option 1")
        elif choice == "2":
            print("You selected Option 2")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


#def clear_screen():
#    print("\033[2J\033[H", end="")

main()