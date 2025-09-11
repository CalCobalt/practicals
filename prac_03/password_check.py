MIN_LENGTH = 6

def get_password():
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password too short, must be at least {MIN_LENGTH} characters.")
        password = input("Enter password: ")
    return password

def print_asterisks(password):
    print("*" * len(password))

def main():
    password = get_password()
    print_asterisks(password)

main()
