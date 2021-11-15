from Domain.cheltuiala import toString
from Logic.CRUD import Adauga_Cheltuiala, stergere_cheltuiala, modificare_cheltuiala
from Logic.functionalitate1 import sterge_toate_cheltuielile_dupa_apart
from Logic.functionalitate2 import Adaugarea_Unei_Val_In_Suma
from Logic.functionalitate3 import Cea_Mai_Mare_Cheltuiala
from Logic.functionalitate4 import Ordonare_Descrescator_Dupa_Suma
from Logic.functionalitate5 import Suma_Pe_Luna


def printMenu():
    print("1. Adauga cheltuiala")
    print("2. Afiseaza toate cheltuielile")
    print("3. Sterge cheltuiala")
    print("4. Modifica cheltuiala")
    print("5. Șterge toate cheltuielile pentru un apartament dat")
    print("6. Adunarea unei valori la toate cheltuielile dintr-o dată citită")
    print("7. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială")
    print("8. Ordonarea cheltuielilor descrescător după sumă.")
    print("9. Afișarea sumelor lunare pentru fiecare apartament.")
    print("u. Undo")
    print("r. Redo")
    print("x. Iesire")


def UI_Adauga_Cheltuiala(lista, undoList, redoList):
    try:
        id = input("Dati id-ul: ")
        nrapart = int(input("Dati apartamentul: "))
        suma = float(input("Dati suma: "))
        data = input("Dati data DD.MM.YYYY: ")
        tip = input("Dati tip-ul: ")
        rezultat = Adauga_Cheltuiala(id, nrapart, suma, data, tip, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def UI_stergere_cheltuiala(lista, undoList, redoList):
    try:
        id = input("Dati id-ul cheltuielii de sters: ")
        rezultat = stergere_cheltuiala(id, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def UI_modificare_cheltuiala(lista, undoList, redoList):
    try:
        id = input("Dati id-ul cheltuielii de modificat: ")
        nrapart = input("Dati noul apartament: ")
        suma = float(input("Dati noua suma: "))
        data = input("Dati noua data DD.MM.YYYY: ")
        tip = input("Dati noul tip: ")
        rezultat = modificare_cheltuiala(id, nrapart, suma, data, tip, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def afisare(lista):
    try:
        for cheltuiala in lista:
            print(toString(cheltuiala))
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def UI_sterge_toate_cheltuielile_dupa_apart(lista, undoList, redoList):
    try:
        nrapart = int(input("Dati numarul apartamentului caruia sa ii se stearga toate cheltuielile: "))
        rezultat = sterge_toate_cheltuielile_dupa_apart(nrapart, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def UI_Adaugarea_Unei_Val_In_Suma(lista, undoList, redoList):
    try:
        data = input("Dati data in format DD.MM.YYYY: ")
        suma = int(input("Dati suma: "))
        Adaugarea_Unei_Val_In_Suma(suma, data, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def UI_Suma_Pe_Luna(lista):
    rezultat = Suma_Pe_Luna(lista)
    for luna in rezultat:
        print("Luna {} are suma preturilor {}".format(luna, rezultat[luna]))

def UI_Ordonare_Descrescator_Dupa_Suma(lista):
    afisare(Ordonare_Descrescator_Dupa_Suma(lista))


def RunMain(lista):
    undoList = []
    redoList = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = UI_Adauga_Cheltuiala(lista, undoList, redoList)
        elif optiune == "2":
            afisare(lista)
        elif optiune == "3":
            lista = UI_stergere_cheltuiala(lista, undoList, redoList)
        elif optiune == "4":
            lista = UI_modificare_cheltuiala(lista, undoList, redoList)
        elif optiune == "5":
            lista = UI_sterge_toate_cheltuielile_dupa_apart(lista, undoList, redoList)
        elif optiune == "6":
            UI_Adaugarea_Unei_Val_In_Suma(lista, undoList, redoList)
        elif optiune == "7":
            Cea_Mai_Mare_Cheltuiala(lista)
        elif optiune == "8":
            UI_Ordonare_Descrescator_Dupa_Suma(lista)
        elif optiune == "9":
            UI_Suma_Pe_Luna(lista)
        elif optiune == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
