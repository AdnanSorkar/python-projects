total_checked = 0

while True:
    password = input("\nEnter a password or 'exit' to quit: ")
    
    if password.lower() == 'exit':
        print(f"\nYou checked {total_checked} password(s) this season.")
        print()
        break
    
    if not password.strip():
        print("Password cannot be empty.")
        continue
        
    print()
    score = 0
    total_checked += 1

    if len(password) >= 8:
        score += 1

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum() and not char.isspace():
            has_symbol = True

    if has_upper:
        score += 1
    else:
        print("Use uppercase letter")

    if has_lower:
        score += 1
    else:
        print("Use lowercase letter")

    if has_digit:
        score += 1
    else:
        print("Use digit")

    if has_symbol:
        score += 1
    else:
        print("Use special symbol")

    if (0 <= score <= 2):
        strength = "Weak"
        print(f"\n'{password}' -> {score}/5 ({strength})")
    elif (2 < score < 5):
        strength = "Medium"
        print(f"\n'{password}' -> {score}/5 ({strength})")
    elif (score == 5):
        strength = "Strong"
        print(f"\n'{password}' -> {score}/5 ({strength})")

    print()