"""Crop base class with common behavior for all crops."""

# pylint: disable=too-few-public-methods


class Crop:
    """Base class for crops that holds common state and behavior."""

    def __init__(self):
        """Initialize a crop with zero grains."""
        self.grains = 0

    def ripe(self):
        """Return True when the crop has enough grains to be considered ripe."""
        return self.grains >= 15
