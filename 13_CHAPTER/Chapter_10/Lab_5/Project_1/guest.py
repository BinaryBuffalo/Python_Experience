print("Add your name to the guest list\n")
msg1 = input("\t~> ")
with open("guest_list.txt", 'a') as f_obj1:
    cmdll = f"\n{msg1}"
    f_obj1.write(cmdll)
print(f"[+] Added {msg1} to the guest list")