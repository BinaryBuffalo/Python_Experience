#Author BakedBinary
#Date 11/5/2021

"""Reads the names in the provided file"""
def read_name(filename):
    try:
        with open(filename) as f:
            content1 = f.read()
    except FileNotFoundError:
        print(f"[x] {filename} Is not a valid filename")
        return 1
    else:
        return content1

print("Usage: help\nEnter 'q' to quit")
while True:
    msgll1 = input("$\t~> ")
    if msgll1 == 'q':
        exit(1)
    if msgll1 == 'help':
        print("\t[Commands]\n")
        print("\t  1. !Cats")
        print("\t  2. !Dogs")
    if msgll1 == "!Cats" or msgll1 == "!Dogs":
        ip_flo = input("\tFile Name: ")
        lizard = read_name(ip_flo)
        if lizard == 1:
            pass
        else:
            total = lizard.split()
            print(f"Total Cats: {len(total)}\nShow Names ? (Yes/No)")
            yes_maybe = input("$\t~> ")
            if yes_maybe == "Yes" or yes_maybe == "yes"or yes_maybe == "Y" or yes_maybe == "y":
                print("\n\t[+] Cats!")
                for item in total:
                    print(f"{item}")
                print("[+]===========[+]")
            else:
                pass
    