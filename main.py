'''
Andrew Fesenko
'''


def encoder(password):
    if len(password) != 8 or not password.isdigit():
        return "Invalid password"
    encoded = [(int(char) + 3) % 10 for char in password]
    return ''.join(map(str, encoded))


'''def decoder(encoded_password):

'''


def main():
    while True:
        print("1. Encode a password")
        print("2. Decode a password")
        print("3. Exit")
        choice = input("Enter your choice")

        if choice == "1":
            password = input("Enter your 8 digit password: ")
            print("Encoded password:", encoder(password))
        elif choice == "2":
            encoded_password = input("Enter your 8 digit password: ")
            print("Decoded password: ", decoder(encoded_password))
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
