class Category:

    def __init__(self, name):
        self.name = name
        self.category = []

    def addFoodToCategory(self, food):
        self.category.append(food)

    def removeFoodFromCategory(self, food):
        self.category.remove(food)

    def getCategory(self):
        return self.category

    def getFood(self, index):
        return self.category[index]

    def getName(self):
        return self.name
