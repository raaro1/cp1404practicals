from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Creates list of objects and prints Menu"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print(f"Let's drive! \n{MENU}")
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "d":
            ...
        elif choice == "d"
            ...
        else
            print("Invalid Option")

        print(MENU)
        choice = input(">>> ").lower()

def drive_taxi(taxi,current_taxi):
    """ """
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return



main()