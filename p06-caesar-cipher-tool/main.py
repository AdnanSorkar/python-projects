from cipher import displayMenu, encrypt, decrypt

while True:
    menu = displayMenu()
    if menu is not None:
        print(menu)
    
    ch = input("Select an option (1-3): ").strip()

    if ch == "1":
        msg = input("Enter message to encrypt: ")
        keyNum = input("Enter shift key (1-25): ").strip()
        try:
            key = int(keyNum)
            if not 1 <= key <= 25:
                print("Shift key must be between 1 and 25.")
                continue
        except ValueError:
            print("Enter a valid whole number.")
            continue

        result = encrypt(msg, key)
        print(f"Encrypted message: {result}")

    elif ch == "2":
        msg = input("Enter message to decrypt: ")
        keyNum = input("Enter shift key (1-25): ").strip()
        try:
            key = int(keyNum)
            if not 1 <= key <= 25:
                print("Shift key must be (1-25).")
                continue
        except ValueError:
            print("Enter a valid whole number.")
            continue

        result = decrypt(msg, key)
        print(f"Decrypted text: {result}")

    elif ch == "3":
        print("Exited from Caesar Cipher Tool.")
        break

    else:
        print("Invalid option. Choose from (1-3).")