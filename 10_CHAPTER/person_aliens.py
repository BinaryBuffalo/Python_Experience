current_aliens = []
while(1):
    blue_length = 0 
    yellow_length = 0
    red_length = 0
    print(f"\tHow many Blue aliens ? ")
    message1 = input("$\t# - > ")
    message1 = int(message1)
    message1 += 1
    for item1 in range(1, message1):
        color1 = {
            'color':'blue',
            }
        current_aliens.append(color1)
    print(f"\tHow many yellow Aliens?")
    message1 = input("$\t# - > ")
    message1 = int(message1)
    message1 += 1
    for item1 in range(1, message1):
        color2 = {
            'color':'yellow',
            }
        current_aliens.append(color2)
    print(f"\tHow many red Aliens ?")
    message1 = input("$\t# - > ")
    message1 = int(message1)
    message1 += 1
    for item1 in range(1, message1):
        color3 = {
            'color':'red',
            }
        current_aliens.append(color3)

    for mathz in current_aliens:
        if (mathz['color'] == 'blue'):
            blue_length += 1
        if (mathz['color'] == 'red'):
            red_length += 1
        if (mathz['color'] == 'yellow'):
            yellow_length += 1
    
    print(f"You have {blue_length} Blue Aliens")
    print(f"You have {yellow_length} Yellow Aliens")
    print(f"You have {red_length} Red Aliens")


print(f"You have {blue_length} Blue Aliens")
    

    
