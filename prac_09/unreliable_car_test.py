from unreliable_car import UnreliableCar

def main():
    """Test to see if drive function works"""
    test_car = UnreliableCar("Miata",100,30)
    for i in range (1,100):
        test_car.drive(i)

    main()