class Band:
    def __init__(self, name):
        """ Create a new Band object """
        self.name = name
        self.musicians = []

    def add_musician(self, musician):
        """Adds a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of a Band object."""
        musicians_str = ", ".join(str(m) for m in self.musicians)
        return f" {self.name} ({musicians_str})"

    def play(self):
        """Return True if the band is currently playing."""
        return "\n".join(m.play() for m in self.musicians)


