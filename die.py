"""A dice implementation for producing rolls."""

from random import randint

class Die:
    """A single dice."""

    def __init__(self, num_sides=6):
        """A six-sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a value from 1 -> no of sides."""
        return randint(1, self.num_sides)