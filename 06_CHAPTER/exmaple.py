alien_1 = {'color': 'green', 'points': 5}
points = alien_1['points']
alien_2 = {}
alien_2['color'] = 'red'
alien_1['points'] = 5
alien_1['x_cord'] = 0
alien_1['y_cord'] = 25
alien_2['x_cord'] = 0
alien_2['y_cord'] = 50
print(f"Alien#1 Layout -> {alien_1}")
print(f"Alien#2 Layout -> {alien_2}")
print(f"\tAlien#1 Color -> {alien_1['color']}")
print(f"\tAlien#2 Color -> {alien_2['color']}")
alien_1['color'] = 'blue'
alien_2['color'] = 'yellow'
print(f"\n\tAlien#1 Color -> {alien_1['color']}")
print(f"\tAlien#2 Color -> {alien_2['color']}")
alien_1['speed'] = 'slow'
alien_2['speed'] = 'medium'
if alien_1 == 'slow':
    x_inc = 1
elif alien_1 == 'medium':
    x_inc = 2
else: #Fast Alien
    x_inc = 3
alien_1['x_cord'] += x_inc
print(f"You have {points} Points")
fav_lang = {
    'joseph': 'C',
    'berry': 'python',
    'kevin': 'Golang',
    }
print(f"Josephs favorite language -> {fav_lang['joseph'].title()}")