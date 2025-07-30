#Work in progress!!!

def encrypt(letter, key):
    return((ord(letter)) + key)


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
        ASCIIqueue = []
        cryptedMessage = ""
        #Loop Through the message
        for x in message:
            ASCIIqueue.append(encrypt(x, key))
            print(x,(ord(x)) ,encrypt(x, key))
        #Shit ASCII Letters by code

