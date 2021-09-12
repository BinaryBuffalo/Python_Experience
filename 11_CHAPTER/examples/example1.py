def greet_user(names):
    """Hello Greeting!"""
    for name in names:
        msg = f"Hello, {name.title()}."
        print(msg)
usernames = ['bob', 'tim', 'tom']
greet_user(usernames)
designes1 = ['black','blue','pink','purple']
designes2 = []
while designes1:
    curdes = designes1.pop()
    print(curdes)
    designes2.append(curdes)
print(designes2)


