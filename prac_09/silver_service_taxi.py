from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """ Adds different classes of taxi services to a Taxi instance. """
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        """ Initialise a Taxi instance, based on parent class Car. """
        super().__init__(name,fuel)
        self.fanciness = fanciness * Taxi.price_per_km

    def calculate_flag_fare(self):



