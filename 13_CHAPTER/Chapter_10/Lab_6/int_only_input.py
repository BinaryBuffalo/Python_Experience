def add_numbers(num1, num2):
    try:
        content = int(num1) + int(num2)
    except ValueError:
        print("[x] Enter a valid input")
    else:
        print(f"Total: {content}")
print("Enter 'q' to Exit")
while True:
    msgll1 = input("\t#1 : ")
    if msgll1 == 'q':
        exit(0)
    msgll2 = input("\t#2 : ")
    if msgll2 == 'q':
        exit(0)
    add_numbers(msgll1, msgll2)
