from src.Food import Food
from src.Category import Category


class Menu:

    vorspeisen = Category("Vorspeisen")
    hauptgerichte = Category("Hauptgerichte")
    nachspeisen = Category("Nachspeisen")
    getreanke = Category("Getraenke")

    def __init__(self, name):
        self.name = name
        self.menu = []
        self.initMenu()

    def initMenu(self):
        self.menu.append(self.vorspeisen)
        self.menu.append(self.hauptgerichte)
        self.menu.append(self.nachspeisen)
        self.menu.append(self.getreanke)

    def printMenu(self):
        for category in self.menu:
            
            print("{}. -{}-".format(self.menu.index(category), category.getName()))
            
            for food in category.getCategory():
                print(food.toString() + "\n")

    def addItem(self):
        for elements in self.menu:
            print("{}. {}".format(self.menu.index(elements), elements.getName()))

        choice = input("Kategorie: ")

        if int(choice) > len(self.menu):
            print("Ungültige Kategorie")
        else:
            name = input("Name: ")
            price = input("Preis: ")
            self.menu[int(choice)].addFoodToCategory(Food(name, price))

    def removeItem(self):
        for elements in self.menu:
            print("{}. {}".format(self.menu.index(elements), elements.getName()))

        choice = input("Kategorie: ")

        print(self.menu[int(choice)].getName())

        for food in self.menu[int(choice)].getCategory():
            print("{}. ".format(self.menu[int(choice)].getCategory().index(food)) + food.toString())

        gericht = input("Gericht: ")

        if int(gericht) > len(self.menu[int(choice)].getCategory()):
            print("Ungültiges Gericht")
        else:
            self.menu[int(choice)].removeFoodFromCategory(
                self.menu[int(choice)].getFood(int(gericht))
            )

    def changeItem(self):
        for elements in self.menu:
            print("{}. {}".format(self.menu.index(elements), elements.getName()))

        delete = input("Kategorie entfernen: ")

        for gerichte in self.menu[int(delete)].getCategory():
            print("{}. ".format(self.menu[int(delete)].getCategory().index(gerichte)) + gerichte.toString())

        gericht = input("Gericht: ")
        for elements in self.menu:
            print("{}. {}".format(self.menu.index(elements), elements.getName()))

        add = input("Kategorie speichern: ")

        if int(gericht) > len(self.menu[int(delete)].getCategory()):
            print("Ungültiges Gericht")
        else:
            self.menu[int(add)].addFoodToCategory(self.menu[int(delete)].getFood(int(gericht)))
            self.menu[int(delete)].removeFoodFromCategory(
                self.menu[int(delete)].getFood(int(gericht)))

    def writeFile(self):
        fileName = input("Dateiname eingeben: ")

        if fileName is str(""):
            file = open("Speisekarte.txt", "w", encoding="utf8")
        else:
            file = open("{}.txt".format(fileName), "w", encoding="utf8")

        for kategorie in self.menu:
            for gerichte in kategorie.getKategorie():
                file.write("{},{},{}\n".format(kategorie.getName(), gerichte.getName(), gerichte.getPrice()))

    def readFile(self):

        with open("Speisekarte.txt") as file:
            for line in file:
                if line != "":
                    (category, name, price) = line.replace("\n", "").split(",")
                    if category == "Vorspeiesen":
                        self.menu[0].addFoodToCategory(Food(name, price))
                    elif category == "Hauptgerichte":
                        self.menu[1].addFoodToCategory(Food(name, price))
                    elif category == "Nachspeisen":
                        self.menu[2].addFoodToCategory(Food(name, price))
                    elif category == "Getraenke":
                        self.menu[3].addFoodToCategory(Food(name, price))
