from robot import turn_left, turn_right, move_forward

direction = input("Write robot direction: ").upper()

for char in direction:
    
    if char == "F" or char == "L" or char == "R":
        continue
    else: break
    