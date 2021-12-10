print("Give me two numbers & i'll divide them\nEnter 'q' to quit ")

while True:
    first_numer = input("\n #1 ~> ")
    if first_numer == 'q':
        exit(0)
        break
    second_numer = input("\n #2 ~> ")
    if second_numer == 'q':
        exit(0)
        break
    try:
        answer = int(first_numer) / int(second_numer)
    except ZeroDivisionError:
        print("you can't divide by 0")
    else:
        print(answer)