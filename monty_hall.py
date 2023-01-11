from random import choice

doors = ["door1", "door2", "door3"]

stay = 0
change = 0

for i in range(10000):
    winning_door = choice(doors)
    selected_door = choice(doors)

    if winning_door == selected_door:
        stay += 1
    else:
        change += 1

change_rate = round((change/10000) * 100,2)
stay_rate = round((stay/10000) * 100,2)

print(f"10000 times of simulation: {change} times win({change_rate}% change) {stay} times win({stay_rate}% stay)")




