"""
Estimate: 15 minutes
Actual: 18 minutes
"""

class ProgrammingLanguage:
    """Gives attributes about the programming language"""
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Checks if the object is dynamic"""
        return self.typing == "Dynamic"


    def __str__(self):
        """Returns a string representation of the object"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year})"