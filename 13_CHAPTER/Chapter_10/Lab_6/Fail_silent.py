print("Provide a file name")
msgll1 = input("$ ~> ")

def count_words(filename):
    """Counts the Number of words in a file"""
    try:
        with open(msgll1, encoding='utf-8') as f:
            obj1 = f.read()
    except FileNotFoundError:
        print(f"[+] {filename} Does not exist")
        pass
    else:
        words = obj1.split()
        num_words = len(words)
        print(f"{filename} Contains: {num_words} Words")

count_words(msgll1)

