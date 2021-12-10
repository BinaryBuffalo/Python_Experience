from os import read


title = "This Sentence has alot of words and so on"
rockll = title.split()
print("Count Words in a file")
msgll1 = input("$ ~> ")
def count_words(filename):
    """Counts the Number of words in a file"""
    try:
        with open(msgll1, encoding='utf-8') as f:
            obj1 = f.read()
    except FileNotFoundError:
        print(f"[+] {filename} Does not exist")
    else:
        words = obj1.split()
        num_words = len(words)
        print(f"{filename} Contains: {num_words} Words")
count_words(msgll1)