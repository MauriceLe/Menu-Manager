class Food:

    food = []

    def __init__(self, name, price):
        self.addFood(name, price)

    def addFood(self, name, price):
        self.food.append(name)
        self.food.append(price)

    def getName(self):
        return self.food[0]

    def getPrice(self):
        return self.food[1]

    def toString(self):
        return "{}: {}".format(self.food[0], self.food[1])
