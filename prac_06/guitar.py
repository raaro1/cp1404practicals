"""
Estimated: 30 minutes
Actual:
"""

CURRENT_YEAR = 2025
VINTAGE_AGE = 50

class Guitar:
    """Adds attributes to newly created objects"""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Returns the age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Checks if object is vintage"""
        return self.get_age() > VINTAGE_AGE

    def __str__(self):
        """Returns a string representation of the object"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"