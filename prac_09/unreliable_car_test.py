from unreliable_car import UnreliableCar

def main():
    """Test to see if drive function works"""
    bad_car = UnreliableCar("Miata",100,30)
    good_car = UnreliableCar("Toyota",100,80)

    for i in range (1,10):
        print(f"{good_car.name} drove {good_car.drive(i)}")
        print(f"{bad_car.name} drove {bad_car.drive(i)}")

main()