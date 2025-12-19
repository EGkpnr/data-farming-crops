"""Rice crop implementation."""

from farm.crop import Crop


class Rice(Crop):
    """Represents a rice crop.

    Watering increases grains by 5 and transplanting increases grains by 10.
    """

    def water(self):
        """Water the rice crop and add 5 grains."""
        self.grains += 5

    def transplant(self):
        """Transplant the rice crop and add 10 grains."""
        self.grains += 10
