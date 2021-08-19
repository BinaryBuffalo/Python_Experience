def make_shirt(sizell, textprint):
    """Creates T-shirt"""
    print(f"\tMens or Womans\n")
    message = input('\t$ -~-~> ')
    print(f"[+]===================[+]")
    if (message == 'mens'):
        print(f"\nType ~> Mens")
        print(f"\nSize ~> {sizell}")
        print(f"\nText ~> {textprint}\n")
        print(f"[+]===================[+]")
    elif (message == 'womans'):
        print(f"\nType -> Womans")
        print(f"\nSize -> {sizell}")
        print(f"\nText -> {textprint}\n")
        print(f"[+]===================[+]")
    else:
        print(f"No shirt selected")
        exit(0)
        ##
print(f"\n[NO CAPS]\nWhat text would you like on your shirt\n")
obj_a1 = input("$\t Message ~~~>   ")
print(f"\n\tWhat size shirt do you where?\n")
print(f"\tSMALL | MEDIUM | LARGE \n")
obj_a2 = input("$   Size ~ > ")
make_shirt(obj_a2, obj_a1)