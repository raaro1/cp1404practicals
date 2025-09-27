MIN_LENGTH = 5

def main():
    """Main function"""
    password = get_password()

    print_stars(password)


def print_stars(password):
    """definite loop that prints (*) the length of the password"""
    for i in range(len(password)):
        print("*", sep=' ', end=' ')


def get_password():
    """Get password from user and validate it"""
    password = str(input("Enter your password: "))
    while len(password) < MIN_LENGTH:
        print("Password must be at least 5 characters long")
        password = str(input("Enter your password: "))
    return password


main()
