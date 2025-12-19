
class Corn:
    # YOUR CODE HERE
    pass


    def __init__(self):
        self.grains = 0
        self.watered = False


    def water(self):
        self.watered = True
        self.grains += 10
        
    def ripe(self):

        return self.grains >= 15