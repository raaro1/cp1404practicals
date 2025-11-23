from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Creates list of objects and prints Menu"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0
    print(f"Let's drive! \n{MENU}")

    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "d":
            trip_cost = drive_taxi(current_taxi)
            bill_to_date += trip_cost
        elif choice == "c":
            current_taxi = choose_taxi(taxis)
        else:
            print("Invalid Option")
    
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: {bill_to_date:.2f}")
    print("Taxis are now:")
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")



def drive_taxi(current_taxi):
    """Uses current taxi to drive given distance"""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0
    else:
        distance = int(input("Drive how far? "))
        current_taxi.start_fare()
        current_taxi.drive(distance)
        trip_cost = current_taxi.get_fare()

        print(f"Your {current_taxi.name} trip will cost you ${trip_cost:.2f}")

        return trip_cost


def choose_taxi(taxis):
    """Chooses a taxi out of a list"""
    print("Taxis available")
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")

    choice = int(input("choose taxi: "))
    if choice > len(taxis) or choice < 0:
        print("Invalid choice")
        return None
    else:
        return taxis[choice]

main()