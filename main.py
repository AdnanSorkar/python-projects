from robot import turn_left, turn_right, move_forward

direction = input("Write robot direction: ").upper()

for char in direction:
    
    if char == "F":
        move_forward()
   
    elif char == "L":
        turn_left()
    
    elif char == "L":
        turn_right()
    
    else:
        print("You have typed wrong letter.")
    
    