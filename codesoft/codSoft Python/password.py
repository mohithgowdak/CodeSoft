import random
import string

def generate_password(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            else:
                password = generate_password(length)
                print(f"Generated password: {password}")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == '__main__':
    main()
