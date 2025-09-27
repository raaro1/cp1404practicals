"""Simple Menu"""
username = str(input("Enter name: "))
print("(H)ello\n(G)oodbye\n(Q)uit")

choice = str(input(">>> ")).upper()
while choice != "H" and choice != "G" and choice != "Q":
    print("invalid choice")
    choice = str(input(">>> ")).upper()

while choice != "Q":

    if choice == "H":
        print(f"Hello {username}")
    elif choice == "G":
        print(f"Goodbye {username}")


    choice = str(input(">>> ")).upper()

print("Finished.")