from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Extension of Car that considers the reliability of the car"""
    def __init__(self,name, fuel,reliability):
        super().__init__(name, fuel)
        self.reliability = reliability


    def drive(self,distance):
        """Determines whether a car can drive based on its reliability"""
        chance = randint(0,100)
        if chance < self.reliability:
            return super().drive(distance)
        else:
            return 0






