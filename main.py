from robot import turn_left, turn_right, move_forward

direction = input("Write robot direction: ").upper().strip()

if not direction:
    print("Direction cannot be empty.")
else:
    for char in direction:
        if char == "F":
            move_forward()
        elif char == "L":
            turn_left()
        elif char == "R":
            turn_right()
        elif not char.isspace():
            print(f"Invalid character '{char}' entered.")