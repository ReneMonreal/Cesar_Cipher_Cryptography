#Work in progress!!!

def encrypt(letter, key):
    return((ord(letter)) + key)
def decrypt(letter, key):
    return((ord(letter)) - key)


print("----------------------------------")
running = True
while(running):
    message = ""
    key = 0
    ASCIIqueue = []
    cryptedMessage = ""
    print(" 1. Encrypt a message")
    print(" 2. Decrypt a message")
    print(" 3. Exit")
    try:
        choice = str(input("Enter your choice (1-3): "))
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 3.")
        continue

    if choice == "1":
        message = input(str("Enter a message you want to encrypt: "))
        try:
            key = int(input("Enter a key (number): "))
        except ValueError:
            print("Invalid key. Please enter a number.")
            continue

        #Convert each letter into ascii nums
        ASCIIqueue = []
        cryptedMessage = ""
        for x in message:
            ASCIIqueue.append(encrypt(x, key))
        
        #nums back into str
        for num in ASCIIqueue:
            cryptedMessage = cryptedMessage + chr(num)
        
        print(f'Coded Message: {cryptedMessage}')

    elif choice == "2": 
        cryptedMessage = str(input(("What is your coded Message?: ")))
        key = int(input("What is your key?: "))
        for x in cryptedMessage:
            ASCIIqueue.append(decrypt(x, key))
        
        for num in ASCIIqueue:
            message = message + chr(num)
        
        print(f"Decoded Message: {message}")

    elif choice == "3":
        running = False

