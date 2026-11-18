def turn_left(heading):
    if heading == "North":
        return "West"
    elif heading == "West":
        return "South"
    elif heading == "South":
        return "East"
    elif heading == "East":
        return "North"
    return heading

def turn_right(heading):
    if heading == "North":
        return "East"
    elif heading == "East":
        return "South"
    elif heading == "South":
        return "West"
    elif heading == "West":
        return "North"
    return heading

def move_forward(x, y, heading):
    x1 = x
    y1 = y

    if heading == "North":
        y1 += 1
    elif heading == "East":
        x1 += 1
    elif heading == "South":
        y1 -= 1
    elif heading == "West":
        x1 -= 1

    if 0 <= x1 <= 4 and 0 <= y1 <= 4:
        print(f"Moved to ({x1}, {y1})")
        return x1, y1
    else:
        print(f"Warning: Blocked at edge ({x}, {y}); facing {heading}")
        return x, y
