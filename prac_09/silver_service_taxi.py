from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Adds different classes of taxi services to a Taxi instance."""
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name,fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km

    def get_fare(self):
        """Return the price for the taxi trip."""
        fare = super().get_fare()
        return fare + self.flag_fall

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flag_fall}"
