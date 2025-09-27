import random

def main():
    MENU = """(G)et a valid score
(P)rint result
(S)how stars (Q)uit"""
    print(MENU)
    choice = input(">>> ").upper()
    score = generate_valid_score()
    while choice != "Q":
        if choice == "G":
            print(f"Your score is: {score}")

        elif choice == "P":
            status = determine_score_status(score)
            print(f"Your result is: {status}")

        elif choice == "S":
            print_stars(score)

        else:
            print("Invalid choice")
            print(MENU)
            choice = input(">>> ").upper()

    print("Thank you for playing, farewell!")

def generate_valid_score():
    """Generates random score and prints status"""
    score = random.randint(1, 100)
    return score


def determine_score_status(score):
    """Determines score status from user's score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """definite loop that prints (*) the length of the score"""
    for i in range(score, + 1):
        print("*", sep=' ', end=' ')

main()