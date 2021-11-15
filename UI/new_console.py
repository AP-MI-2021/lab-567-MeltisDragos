from Logic.CRUD import Adauga_Cheltuiala, stergere_cheltuiala, modificare_cheltuiala
from UI.console import afisare


def menu(lista):
    undoList = []
    redoList = []
    while True:
        comanda = input("Introduceti comenzile, separate prin ; :")
        optiuni = comanda.split(";")
        if comanda == "help":
            print("Add,id,nrapartament,suma,data,tip: adauga cheltuiala")
            print("Delete,id: sterge cheltuiala")
            print("Update,id: modifica cheltuiala")
            print("ShowAll: afiseaza cheltuielile")
            print("Undo: Sterge ultima comada")
            print("Redo: Readuce ultima comanda")
            print("Exit: opreste program")
        elif optiuni[0] == "Exit":
            break
        else:
            for optiune in optiuni:
                functie = optiune.split(",")
                if functie[0] == "Add":
                    try:
                        undoList.append(lista)
                        redoList.clear()
                        lista = Adauga_Cheltuiala(functie[1], functie[2], functie[3], functie[4], functie[5], lista)
                    except IndexError as ie:
                        print("Eroare: {}".format(ie))
                    except ValueError as ve:
                        print("Eroare: {}".format(ve))
                elif functie[0] == "Delete":
                    try:
                        undoList.append(lista)
                        redoList.clear()
                        lista = stergere_cheltuiala(functie[1], lista)
                    except ValueError as ve:
                        print("Eroare: {}".format(ve))
                elif functie[0] == "Update":
                    try:
                        undoList.append(lista)
                        redoList.clear()
                        lista = modificare_cheltuiala(functie[1], functie[2], functie[3], functie[4], functie[5], lista)
                    except ValueError as ve:
                        print("Eroare: {}".format(ve))
                elif functie[0] == "ShowAll":
                    afisare(lista)
                elif functie[0] == "Undo":
                    if len(undoList) > 0:
                        redoList.append(lista)
                        lista = undoList.pop()
                    else:
                        print("Nu se poate face undo!")
                elif functie[0] == "Redo":
                    if len(redoList) > 0:
                        undoList.append(lista)
                        lista = redoList.pop()
                    else:
                        print("Nu se poate face redo!")
                else:
                    print("Optiune gresita! Foositi comada 'help'. ")
