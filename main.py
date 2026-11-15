while True:
    password = input("\nEnter a password or 'exit' to quit: ")
    
    if password.lower() == 'exit':
        print()
        break
        
    print()
    score = 0

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
        elif not char.isalnum():
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
        print("\nWeak")
    elif (3 <= score <= 4):
        print("\nMedium")
    elif (score == 5):
        print("\nStrong")

    print()