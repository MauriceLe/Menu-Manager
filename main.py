from src.Menu import Menu


def __main__():

    speisekarte = Menu("Speisekarte 1")
    close = False

    while close is False:

        speisekarte.readFile()

        print("\na = Speisekarte anzeigen \nn = neues Gericht hinzufügen \ne = Programmende \nl = Gericht löschen \nk = Kategorie ändern \n")
        choice = input("Auswahl tätigen: ")
        print(" ")

        if choice == "a":
            speisekarte.printMenu()
        elif choice == "n":
            speisekarte.addItem()
        elif choice == "l":
            speisekarte.removeItem()
        elif choice == "k":
            speisekarte.changeItem()
        elif choice == "e":
            close = True
            speisekarte.writeFile()


if __name__ == "__main__":
    __main__()
