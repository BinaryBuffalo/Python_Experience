# Author: Baked Binary
# Shows 2 list in Reverse, Alphabetical & Reverse  
world = ["canada", "mexico", "england", "russia"]
print(world)
print(f"\n\tSorted list -> {sorted(world)}")
print(f"\n\tOriginal    -> {world}")
print(f"\n\tReverse     -> {sorted(world, reverse=True)}")
print(f"\n\tOriginal    -> {world}")
places = ["spain", "germany", "france", "poland"]
print(f"Places -> {places}")
places.reverse()
print(f"List Reverses -> {places}")
places.reverse()
print(f"List Original -> {places}")
places.sort()
print(f"Alphabetical  -> {places}")
places.sort(reverse=True)
print(f"Reversed      -> {places}")

