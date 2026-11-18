from robot import turn_left, turn_right, move_forward

x = 0
y = 0
heading = "NORTH"

direction = input("Write robot direction: ").upper().strip()

if not direction:
    print("Direction cannot be empty.")
else:
    for char in direction:
        if char == "F":
            x, y = move_forward(x, y, heading)
        elif char == "L":
            heading = turn_left(heading)
        elif char == "R":
            heading = turn_right(heading)
        elif not char.isspace():
            print(f"Invalid character '{char}' entered.")

print(f"Final Position: ({x}, {y}) facing {heading}")