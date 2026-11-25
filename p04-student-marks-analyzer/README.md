# Student Marks Analyzer

A command-line Python program that collects student marks, calculates summary statistics, assigns letter grades, and prints a formatted report.

## Grade Scale

- A: 80 – 100
- B: 70 – 79.9
- C: 60 – 69.9
- D: 40 – 59.9 (Passing threshold)
- Fail: Below 40

## Features

- Collects student marks interactively until the user types exit (using 1-based student numbering).
- Validates input to handle empty entries, non-numeric values (ValueError), and marks outside 0 to 100.
- Calculates class average (rounded to 2 decimal places), highest mark, lowest mark, total passed students, and pass percentage.
- Safely handles empty mark lists without crashing.
- Prints a final summary and an individual grade report for each student.

## How to Run

Make sure both main.py and analyzer.py are in the same project folder, then run:

python main.py


## Sample Input and Output

Enter students' numbers / type 'exit' :
Enter #1 student's number: 85
Enter students' numbers / type 'exit' :
Enter #2 student's number: 72
Enter students' numbers / type 'exit' :
Enter #3 student's number: 35
Enter students' numbers / type 'exit' :
Enter #4 student's number: exit

Average: 64.0
Highest: 85.0
Lowest: 35.0
Total passed: 2
Passed percentage: 66.67 %

Final Report of 3 student(s):
Student #1: 85.0 -> Grade: A
Student #2: 72.0 -> Grade: B
Student #3: 35.0 -> Grade: Fail


## What I Learned

- Structuring a Python project across multiple files (main.py for CLI input/reporting and analyzer.py for calculation and grading functions).
- Working with lists, append(), indexing, len(), sum(), min(), max(), and round().
- Using try / except ValueError and empty-list checks (if not stdList:) to prevent crashes on invalid or empty input.
- Writing clear conditional logic (if / elif / else) for letter grades and pass counts.

## Future Improvements

- Store student names alongside their marks.
- Export the final report to a text or CSV file.
- Add unit tests in docs/test_cases.md to cover all edge cases.