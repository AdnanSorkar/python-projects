# CLI Task Manager (`p05-cli-task-manager`)

## Summary

A modular, menu-driven Command-Line Interface (CLI) task manager built in Python. It separates user input and loop control (`main.py`) from core task state logic (`tasks.py`), allowing users to add tasks, list tasks with completion status, toggle completion, and delete tasks by number.

### Sample Menu

```text
Menu:

1. Include
2. List
3. Done
4. Remove
5. Exit
```

---

## Features

- **Include Tasks (`1`):** Adds new tasks (trimmed and normalized to lowercase) with a default `Not done` status while rejecting empty inputs.
- **List Tasks (`2`):** Displays all tasks with 1-based numbering alongside their `Done` or `Not done` status, or notifies when the list is empty.
- **Mark Done / Not Done (`3`):** Updates a task's status (`yes`/`y` -> `Done`, `no`/`n` -> `Not done`) via case-insensitive name matching.
- **Remove Tasks (`4`):** Deletes a task by its 1-based task number with checks for empty input, non-numeric entries, and out-of-range numbers.
- **Exit (`5`):** Exits the interactive CLI loop cleanly.

---

## How to Run

1. Make sure **Python 3** is installed on your system.
2. Open a terminal or command prompt and navigate to the project directory:
   ```bash
   cd p05-cli-task-manager
   ```
3. Run the application:
   ```bash
   python main.py
   ```

---

## Example Session

```text
Menu:

1. Include
2. List
3. Done
4. Remove
5. Exit

Select a option: 1
Enter a task: Study Python
Task (1) 'study python' is added.

Menu:

1. Include
2. List
3. Done
4. Remove
5. Exit

Select a option: 1
Enter a task: Build CLI project
Task (2) 'build cli project' is added.

Menu:

1. Include
2. List
3. Done
4. Remove
5. Exit

Select a option: 2
(1) 'study python' is Not done
(2) 'build cli project' is Not done

Menu:

1. Include
2. List
3. Done
4. Remove
5. Exit

Select a option: 3
Enter task name: study python
Enter task done or not (yes/no): yes
'study python' is done.

Menu:

1. Include
2. List
3. Done
4. Remove
5. Exit

Select a option: 4
Enter the task no. to delete: 2
Task (2) 'build cli project' is deleted.

Menu:

1. Include
2. List
3. Done
4. Remove
5. Exit

Select a option: 5
```

---

## What I Learned

- **Separation of Concerns:** Keeping all `input()` prompts and loop control in `main.py` while keeping state-mutating functions in `tasks.py` makes functions cleaner, modular, and easier to test.
- **Consistent State Flow:** Returning the updated `tasks` list from every state-modifying function and reassigning `tasks = ...` in `main.py` keeps data flow predictable.
- **Defensive Input Validation:** Handling empty strings, `ValueError` exceptions during `int()` conversion, and 1-based vs. 0-based index bounds prevents runtime crashes.
- **Data Representation:** Using a nested list structure (`[[title, completed], ...]`) with `enumerate(..., start=1)` cleanly pairs human-friendly task numbers with boolean states.

---

## Future Improvements

- **Persistent Storage:** Save and load tasks using a JSON or text file so tasks persist after exiting the program.
- **Preserve Original Title Casing:** Store the user's original capitalization for task titles while keeping search comparisons case-insensitive.
- **Mark Done by Task Number:** Allow marking tasks as done/not done using their task number in addition to their task name.
- **Automated Unit Tests:** Add `pytest` or `unittest` test suites for all functions in `tasks.py`.