def sql_vulnerability():
    # Functionality for SQL Vulnerability
    print("Executing SQL Vulnerability Tool")


def self_raid():
    # Functionality for Self Raid
    print("Executing Self Raid Tool")


def discord_raid():
    # Functionality for Discord Raid
    print("Executing Discord Raid Tool")


def bot_raid():
    # Functionality for Bot Raid
    print("Executing Bot Raid Tool")


def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. SQL Vulnerability")
        print("2. Self Raid")
        print("3. Discord Raid")
        print("4. Bot Raid")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            sql_vulnerability()
        elif choice == '2':
            self_raid()
        elif choice == '3':
            discord_raid()
        elif choice == '4':
            bot_raid()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main_menu()