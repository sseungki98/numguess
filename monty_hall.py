from random import choice

doors = ["door1", "door2", "door3"]

stay = 0
change = 0
    
winning_door = choice(doors)
selected_door = choice(doors)

if winning_door == selected_door:
    stay += 1
else:
    change += 1




