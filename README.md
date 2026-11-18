### Robot Grid Navigator (p03-robot-grid-navigator)

A command-line Python simulator that navigates a robot across a 5x5 grid using directional commands while preventing out-of-bounds movement.

## Grid Layout

The grid ranges from coordinate `(0, 0)` to `(4, 4)`. The robot starts at `(0, 0)` facing `North`:

y
4 | .  .  .  .  .
3 | .  .  .  .  .
2 | .  .  .  .  .
1 | .  .  .  .  .
0 | R  .  .  .  .
  +---------------
    0  1  2  3  4  x


## Commands

F — Move forward one step in the current heading direction.
L — Turn 90 degrees left (counter-clockwise).
R — Turn 90 degrees right (clockwise).

## How to Run

Ensure both main.py and robot.py are in the same folder, then run the program from your terminal using:

`python main.py`


## Sample Commands and Output

Write robot direction: ffrf

Moved to (0, 1)
Moved to (0, 2)
Moved to (1, 2)

Final Position: (1, 2); facing East

## What I Learned

Separating pure logic (robot.py) from user input and output (main.py).

Passing and returning state variables (x, y, heading) between functions instead of using global variables.

Using temporary boundary variables (x1, y1) to safely validate grid limits before updating the robot's actual position.

## Next Idea

```Obstacles:``` Add static obstacle coordinates on the 5x5 grid that the robot must detect and avoid, similar to boundary edges.