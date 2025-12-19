"""Corn crop implementation."""

from farm.crop import Crop

class Corn(Crop):
    """Represents a corn crop.

    Watering increases grains by 10.
    """

    def water(self):
        """Water the corn crop and add 10 grains."""
        self.grains += 10
