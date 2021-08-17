polls = {
    'arin':'C',
    'joe':'python',
    'tim':'roby',
    'dan':'html',
    'tommy':'css',
    }
list1 = ["danny","jarred"]
i = 0
for item in polls.keys():
    if item in polls:
        print(f"{item}, Thanks for taking the poll\n")
    if i == 0 or i == 1:
        print(f"{list1[i]}, Please Take the poll\n")
        i += 1

