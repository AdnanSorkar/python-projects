# **Password Strength Checker**

A simple Python program that checks how strong a password is. It gives a score from 0 to 5, rates it as **Weak**, **Medium**, or **Strong**, and shows tips on how to make it better.

## **The 5 Scoring Rules**

1. Length (at least 8 characters)
2. Uppercase letter (`A-Z`)
3. Lowercase letter (`a-z`)
4. Numeric digit (`0-9`)
5. Special symbol (excluding spaces)

## **Scoring**

- **0-2:** Weak
- **3-4:** Medium
- **5:** Strong

## **How to Run**

Run the program from your terminal using:
python main.py

## **Sample Runs (Fake Passwords Only)**

Enter a password or 'exit' to quit: f43

Use uppercase letter
Use special symbol

'f43' -> 2/5 (Weak)


Enter a password or 'exit' to quit: exit

You checked 1 password(s) this season.

## **Safety Note**

> **Never type your real passwords into this tool.** Only use fake passwords for testing.

## **What I Learned**

- How to check strings and loop through characters in Python.
- How to use `True`/`False` flags to count rules.
- How to save and track my work using Git.

## **Future Improvements**

- Warn the user if they type a very common password (like `123456` or `password`).
- Add an option to hide the password while typing.