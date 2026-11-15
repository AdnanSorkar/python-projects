# **Password Strength Checker**

A simple Python program that checks how strong a password is. It gives a score from 0 to 5, rates it as **Weak**, **Medium**, or **Strong**, and shows tips on how to make it better.

## **The 5 Scoring Rules**

1. **Length:** At least 8 characters long.
2. **Uppercase:** Has at least one capital letter (`A-Z`).
3. **Lowercase:** Has at least one small letter (`a-z`).
4. **Digit:** Has at least one number (`0-9`).
5. **Symbol:** Has at least one special character (like `!`, `@`, `#`, `$`).

## **Scoring**

- **0-2:** Weak
- **3-4:** Medium
- **5:** Strong

## **How to Run**

Run the program from your terminal using:
python main.py

## **Sample Runs (Fake Passwords Only)**

- Input: `abc` -> **1/5 (Weak)** - *Tip: Make it longer and add capitals, numbers, and symbols.*
- Input: `Password1` -> **4/5 (Medium)** - *Tip: Add a symbol.*
- Input: `Dhaka2026!` -> **5/5 (Strong)** - *Great password!*

## **Safety Note**

> **Never type your real passwords into this tool.** Only use fake passwords for testing.

## **What I Learned**

- How to check strings and loop through characters in Python.
- How to use `True`/`False` flags to count rules.
- How to save and track my work using Git.

## **Future Improvements**

- Warn the user if they type a very common password (like `123456` or `password`).
- Add an option to hide the password while typing.