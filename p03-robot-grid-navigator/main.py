from robot import turn_left, turn_right, move_forward

x = 0
y = 0
heading = "North"
warning_count = 0

direction = input("\nWrite robot direction: ").upper().strip()
print()

if not direction:
    print("Direction cannot be empty.")

else:
    for char in direction:
        if char == "F":
            x, y, warned = move_forward(x, y, heading)
            if warned:
                warning_count += 1
        elif char == "L":
            heading = turn_left(heading)
            print(f"Moved to ({x}, {y}); facing {heading}")
        elif char == "R":
            heading = turn_right(heading)
            print(f"Moved to ({x}, {y}); facing {heading}")
        elif not char.isspace():
            print(f"Invalid character '{char}' entered.")

print()
if warning_count > 0:
    print(f"Final position: ({x}, {y}) {heading}, {warning_count} edge warning(s)")
else:
    print(f"Final position: ({x}, {y}); facing {heading}")
print()