"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    """Gets user's score and prints status"""
    score = float(input("Enter score: "))
    status = determine_score_status(score)
    print(f"{status}")

    generate_random_score()


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

def generate_random_score():
    """Generates random score and prints status"""
    random_score = random.randint(1, 100)
    random_status = determine_score_status(random_score)
    print(random_status)


main()
