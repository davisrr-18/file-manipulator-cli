import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_file():
    clear_screen()
    print("WARNING: If you create a file with an existing name, the content will be overwritten!")
    confirm = input("Do you wish to continue? (y/n): ").lower().strip()

    if confirm == "y":
        try:
            filename = input("\nEnter the filename: ")
            with open(filename, "w") as file:
                content = input("Enter the text you want to add: ").capitalize()
                file.write(content)
                print("\nFile created successfully.")
        except Exception as error:
            print(f"An error occurred: {error}")
    input("\nPress Enter to continue...")

def read_file():
    clear_screen()
    filename = input("Enter the name of the file you want to read: ")
    try:
        with open(filename, "r") as file:
            print("\n--- File Content ---")
            print(file.read())
            print("--------------------")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as error:
        print(f"An error occurred: {error}")
    input("\nPress Enter to continue...")

def edit_file():
    clear_screen()
    print("INFO: This will append text to the end of the file.")
    filename = input("\nEnter the name of the file you want to edit: ")
    
    if os.path.exists(filename):
        try:
            with open(filename, "a") as file:
                content = input("Enter the text to append: ").capitalize()
                file.write("\n" + content)
                print("File updated successfully.")
        except Exception as error:
            print(f"An error occurred: {error}")
    else:
        print("Error: File not found.")
    input("\nPress Enter to continue...")

def delete_file():
    clear_screen()
    filename = input("Enter the name of the file you want to delete: ")
    confirm = input(f"Are you sure you want to delete '{filename}'? (y/n): ").lower().strip()

    if confirm == "y":
        try:
            os.remove(filename)
            print("File deleted successfully.")
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as error:
            print(f"An error occurred: {error}")
    input("\nPress Enter to continue...")

while True:
    clear_screen()
    print("---------- File Manager CLI ----------")
    print("1. Create New File")
    print("2. Read File")
    print("3. Edit File (Append)")
    print("4. Delete File")
    print("5. Exit")
    print("--------------------------------------")

    try:
        option = input("Select an option (1-5): ").strip()

        if option == "1":
            create_file()
        elif option == "2":
            read_file()
        elif option == "3":
            edit_file()
        elif option == "4":
            delete_file()
        elif option == "5":
            print("Exiting... See you later!")
            break
        else:
            print("Invalid option.")
            input("Press Enter to try again...")
    except Exception as error:
        print(f"Unexpected error: {error}")
        input("Press Enter to continue...")