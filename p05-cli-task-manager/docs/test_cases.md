# Test Cases — CLI Task Manager (`p05-cli-task-manager`)

## Overview
This document outlines manual test cases for verifying `main.py` and `tasks.py`, covering menu navigation, task creation, listing, completion status updates, deletion, and input validation.

---

## 1. Menu & Main Loop (`main.py`)

| ID | Scenario | Input | Expected Output / Behavior |
| :--- | :--- | :--- | :--- |
| TC-01 | Display menu on start / after action | Loop runs | Prints `Menu:` followed by options `1. Include` through `5. Exit`. |
| TC-02 | Empty menu selection | `""` or `"   "` | Prints `Empty input. Try again.` and re-prompts. |
| TC-03 | Non-numeric menu selection | `"abc"` | Prints `Give a number. Try again.` and re-prompts. |
| TC-04 | Out-of-range menu number (low) | `"0"` or `"-2"` | Prints `Invalid option. Choose a number from 1 to 5.` and re-prompts. |
| TC-05 | Out-of-range menu number (high) | `"6"` | Prints `Invalid option. Choose a number from 1 to 5.` and re-prompts. |
| TC-06 | Exit program | `"5"` | Breaks out of the `while` loop and terminates cleanly. |

---

## 2. Add Task (`include_task` / Option `1`)

| ID | Scenario | Input | Expected Output / Behavior |
| :--- | :--- | :--- | :--- |
| TC-07 | Add valid task | `"1"`, then `"Buy Groceries"` | Normalizes to `"buy groceries"`, appends `["buy groceries", False]`, prints `Task (1) 'buy groceries' is added.`. |
| TC-08 | Add multiple tasks | `"1"` -> `"Read Book"`, `"1"` -> `"Workout"` | Appends both with `False` status; second prints `Task (2) 'workout' is added.`. |
| TC-09 | Empty task input | `"1"`, then `"   "` | Does not add a task; prints `Entered empty input. Task not added.`. |

---

## 3. List Tasks (`all_tasks` / Option `2`)

| ID | Scenario | Precondition | Input | Expected Output / Behavior |
| :--- | :--- | :--- | :--- | :--- |
| TC-10 | Empty task list | `tasks = []` | `"2"` | Prints `No tasks found.`. |
| TC-11 | Populated task list (mixed status) | `["buy groceries", False]`, `["workout", True]` | `"2"` | Prints `(1) 'buy groceries' is Not done` and `(2) 'workout' is Done`. |

---

## 4. Mark Task Done / Not Done (`comp_tasks` / Option `3`)

| ID | Scenario | Input | Expected Output / Behavior |
| :--- | :--- | :--- | :--- |
| TC-12 | Mark existing task as done (`yes`) | `"3"`, task name `"Buy Groceries"`, status `"yes"` | Updates status to `True`; prints `'buy groceries' is done.`. |
| TC-13 | Mark existing task as done (`y`) | `"3"`, task name `"workout"`, status `"Y"` | Updates status to `True`; prints `'workout' is done.`. |
| TC-14 | Mark completed task as not done (`no` / `n`) | `"3"`, task name `"buy groceries"`, status `"no"` | Updates status to `False`; prints `'buy groceries' is not done.`. |
| TC-15 | Task not found | `"3"`, task name `"nonexistent"`, status `"yes"` | Prints `'nonexistent' not found.` without modifying tasks. |
| TC-16 | Invalid done/not input | `"3"`, task name `"buy groceries"`, status `"maybe"` | Prints `Invalid input. Type (yes/no).` without changing status. |

---

## 5. Delete Task (`del_task` / Option `4`)

| ID | Scenario | Input | Expected Output / Behavior |
| :--- | :--- | :--- | :--- |
| TC-17 | Delete valid task number | `"4"`, then `"1"` | Removes task `1` from list; prints `Task (1) '<title>' is deleted.`. |
| TC-18 | Empty delete input | `"4"`, then `""` | Prints `Nothing is deleted.` without modifying list. |
| TC-19 | Non-numeric delete input | `"4"`, then `"two"` | Prints `Please enter a valid number.` without modifying list. |
| TC-20 | Task number too low (`0` or negative) | `"4"`, then `"0"` | Prints `Task number is out of range.` without modifying list. |
| TC-21 | Task number too high | `"4"`, then `"99"` | Prints `Task number is out of range.` without modifying list. |