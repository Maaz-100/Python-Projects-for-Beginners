import os


def menu():
    file_name = input("What is the name of the file you want to open or create ")

    if os.path.exists(file_name):
        while True:
            option = input(" would you like to read or write or delete the file . r/w/d or 0 to close ").lower()
            if option in ["r", "d", "w" , "0"]:
                break
            else:
                print(" chose either r/d/w")

        if option == "r":
            read(file_name)
        elif option == "w":
            write(file_name)
        elif option == "d":
            delete(file_name)
        elif option == "0":
            quit()

    else:
        print("this file does not exist, we will create a file named", file_name)
        make_file(file_name)


def delete(file_name):
    while True:
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"{file_name} has been deleted")
        else:
            print("file doesn't exist")
        menu()


def write(file_name):
    with open(file_name, "r+") as file:
        content = file.read()

        print("This is what the file says:")
        print(content)

        # Move the cursor to the end of the file
        file.seek(0, os.SEEK_END)

        # Write to the file
        new_content = input("Enter the new content to add to the file: ")
        file.write("\n" + new_content)

        # Close the file
        file.close()
        menu()


def make_file(file_name):
    with open(file_name, "w") as file:
        file.close()
        menu()


def read(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        print(content)
        menu()


menu()
