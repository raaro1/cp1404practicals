"""
emails
Estimate: 40 minutes
Actual:   37 minutes
"""

EMAIL_TO_NAME = {}

email = input("Email: ")
while email != "":
    email_address = email
    username = email.split("@")[0]
    name_parts = username.split(".")
    name = " ".join(part.title() for part in name_parts)

    user_confirms_name = input(f"Is your name {name}? (Y/n) ").lower()
    if user_confirms_name in ("y",""):
        EMAIL_TO_NAME[email] = name
    else:
        name = input("What is your name? ").title()
        EMAIL_TO_NAME[email] = name

    email = input("Email: ")

print()

for email, name in EMAIL_TO_NAME.items():
    print(f"{name}: {email}")
