"""Password Checker"""
MIN_LENGTH = 5
password = str(input("Enter your password: "))
while len(password) < MIN_LENGTH:
    print("Password must be at least 5 characters long")
    password = str(input("Enter your password: "))

for i in range(len(password)):
    print("*", sep=' ', end=' ')


