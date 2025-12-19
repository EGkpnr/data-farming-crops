
class Rice():
        # YOUR CODE HERE
    pass
    def __init__(self):
        self.grains = 0
        self.watered = False
        self.transplanted = False

    def water(self):
        self.watered = True
        self.grains += 5

    def transplant(self):
        if self.watered:
            self.transplanted = True
            self.grains += 10

    def ripe(self):
        return self.grains >= 15