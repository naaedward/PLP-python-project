def read_and_modify_file():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, 'r') as f:
            content = f.read()
            modified_content = content.upper()  
        with open('modified_' + filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"Modified file saved as: modified_{filename}")
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: File could not be read or written.")

read_and_modify_file()