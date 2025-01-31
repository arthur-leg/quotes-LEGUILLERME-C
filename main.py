from functions import *

def menu():
    print("\n==== Programming Quotes ====")
    print("1. Random quote")
    print("2. Display quotes")
    print("3. Exit")
    print("4 add quotes")

def main():
    while True:
        quotes = load_quotes("quotes.txt")
        menu()

        choice = input("Choose your an action (1-4): ")
        
        if choice == "1":
            print_quote(random_quote(quotes))
        elif choice == "2": # gestion de display_count()
            count = int(input("Enter the number of quotes to display: "))
            display_quotes(quotes, count)
        elif choice == "3":
            print("Good bye...")
        elif choice == "4":
            add_quote(quotes, "quotes.txt")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
