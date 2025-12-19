# pylint: disable=too-few-public-methods


class Crop:
    pass  # YOUR CODE HERE

    """A base class for crops."""

    def __init__(self):
        self.watered = False
        self.grains = 0
        self.ripe = False

    def water(self):
        """Water the crop."""
        self.watered = True
        self.grains += 100  

        self.ripe = True 