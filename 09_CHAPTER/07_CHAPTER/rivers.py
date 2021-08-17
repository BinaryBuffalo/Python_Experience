rivers = {
    'nile':'Egypt',
    'amazon River': 'South America',
    'yangtze':'China',
    'yellow river':'Tibet',
    'congo river':'Africa',
    }
rivers2 = ['nile', 'congo river']
for river in rivers.keys():
    print(f"Rivers -> {river}")
    if river in rivers2:
        name = rivers[river].title()
        print(f"The {river} is located in {name}")
#for key, value in rivers.items():
#    print(f"The {key} river is located in {value}")
