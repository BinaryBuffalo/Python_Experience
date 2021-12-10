from name_function import get_formatted_name

print("Enter 'q' to Exit")
while True:
    firstname = input("First Name: ")
    if firstname == 'q':
        exit(1)

    lastname = input("Last Name : ")
    if lastname == 'q':
        exit(1)

    formated_name = get_formatted_name(firstname, lastname)
    print(formated_name)