import json

numbers = [2, 5, 8, 7, 16, 13]

filename = 'numbers.json'
"""Write Numbers to number.json"""
with open(filename, 'w') as f:
    json.dump(numbers, f)
print("[!] Created numbers.json")
"""Reads Numbers from number.json"""
with open(filename) as f2:
    numbers = json.load(f2)
print("[+] Complete")
print(numbers)
