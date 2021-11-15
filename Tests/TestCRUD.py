from Domain.cheltuiala import get_id, get_nrapart, get_suma, get_data, get_tip
from Logic.CRUD import Adauga_Cheltuiala, getById, stergere_cheltuiala, modificare_cheltuiala
from Logic.functionalitate2 import Adaugarea_Unei_Val_In_Suma
from Logic.functionalitate3 import Cea_Mai_Mare_Cheltuiala
from Logic.functionalitate4 import Ordonare_Descrescator_Dupa_Suma


def test_Adauga_Cheltuieli():
    lista = []
    lista = Adauga_Cheltuiala("1", 21, 179.59, "20.03.2002", "intretinere", lista)
    assert len(lista) == 1
    assert get_id(getById("1", lista)) == "1"
    assert get_nrapart(getById("1", lista)) == 21
    assert get_suma(getById("1", lista)) == 179.59
    assert get_data(getById("1", lista)) == "20.03.2002"
    assert get_tip(getById("1", lista)) == "intretinere"


test_Adauga_Cheltuieli()


def test_stergere_cheltuiala():
    lista = []
    lista = Adauga_Cheltuiala("1", 27, 273.07, "09.04.2000", "canal", lista)
    lista = Adauga_Cheltuiala("2", 30, 30.40, "27.09.1980", "alte cheltuieli", lista)

    lista = stergere_cheltuiala("1", lista)
    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None


test_stergere_cheltuiala()


def test_modificare_cheltuiala():
    lista = []
    lista = Adauga_Cheltuiala("1", 27, 273.07, "09.04.2000", "canal", lista)
    lista = Adauga_Cheltuiala("2", 30, 30.40, "27.09.1980", "alte cheltuieli", lista)
    lista = modificare_cheltuiala("1", 28, 2, "12.12.1212", "intretinere", lista)
    assert get_id(getById("1", lista)) == "1"
    assert get_nrapart(getById("1", lista)) == 28
    assert get_suma(getById("1", lista)) == 2
    assert get_data(getById("1", lista)) == "12.12.1212"
    assert get_tip(getById("1", lista)) == "intretinere"


test_modificare_cheltuiala()


def test_functionalitate2():
    lista = []
    lista = Adauga_Cheltuiala("1", 27, 273.07, "09.04.2000", "canal", lista)
    lista = Adauga_Cheltuiala("2", 30, 30.40, "27.09.1980", "alte cheltuieli", lista)
    lista =Adaugarea_Unei_Val_In_Suma("27.09.1980", 200, lista)
    assert get_suma(list[2]) == 230.40


def test_functionalitate3():
    lista = []
    lista = Adauga_Cheltuiala("1", 27, 273.07, "09.04.2000", "canal", lista)
    lista = Adauga_Cheltuiala("2", 30, 30.40, "27.09.1980", "alte cheltuieli", lista)
    lista = Adauga_Cheltuiala("3", 12, 52.32, "12.12.2012", "canal", lista)
    lista = Adauga_Cheltuiala("4", 12, 32.12, "12.12.2012", "intretinere", lista)
    assert Cea_Mai_Mare_Cheltuiala(lista) == [273.07, 32.12, 30.40]


def test_undo_redo():
    lista = []
    undoList = []
    redoList = []
    lista = Adauga_Cheltuiala("1", 27, 273.07, "09.04.2000", "canal", lista)
    undoList.append(lista)
    redoList.clear()
    lista = Adauga_Cheltuiala("2", 30, 30.40, "27.09.1980", "alte cheltuieli", lista)
    undoList.append(lista)
    redoList.clear()
    lista = Adauga_Cheltuiala("3", 12, 52.32, "12.12.2012", "canal", lista)
    undoList.append(lista)
    redoList.clear()

    assert len(lista) == 3
    assert len(undoList) == 3

    redoList.append(lista)
    undoList.pop()

    assert len(undoList) == 2
    assert len(redoList) == 1

    redoList.append(lista)
    undoList.pop()

    assert len(undoList) == 1
    assert len(redoList) == 2

    redoList.append(lista)
    undoList.pop()

    assert len(undoList) == 0
    assert len(redoList) == 3

    redoList.clear()
    lista.clear()

    Adauga_Cheltuiala("1", 27, 273.07, "09.04.2000", "canal", lista)
    undoList.append(lista)
    redoList.clear()
    Adauga_Cheltuiala("2", 30, 30.40, "27.09.1980", "alte cheltuieli", lista)
    undoList.append(lista)
    redoList.clear()
    Adauga_Cheltuiala("3", 12, 52.32, "12.12.2012", "canal", lista)
    undoList.append(lista)
    redoList.clear()

    assert len(undoList) == 3
    assert len(redoList) == 0

    redoList.append(lista)
    undoList.pop()

    assert len(undoList) == 2
    assert len(redoList) == 1

    redoList.append(lista)
    undoList.pop()

    assert len(undoList) == 1
    assert len(redoList) == 2

    redoList.pop()
    undoList.append(lista)
    assert len(undoList) == 2
    assert len(redoList) == 1

    redoList.pop()
    undoList.append(lista)
    assert len(undoList) == 3
    assert len(redoList) == 0

    undoList.pop()
    redoList.append(lista)
    assert len(undoList) == 2
    assert len(redoList) == 1

    undoList.pop()
    redoList.append(lista)
    assert len(undoList) == 1
    assert len(redoList) == 2

    Adauga_Cheltuiala("2", 30, 30.40, "27.09.1980", "alte cheltuieli", lista)
    undoList.append(lista)
    redoList.clear()

    assert len(undoList) == 2
    assert len(redoList) == 0

    undoList.pop()
    redoList.append(lista)
    assert len(undoList) == 1
    assert len(redoList) == 1

    undoList.pop()
    redoList.append(lista)
    assert len(undoList) == 0
    assert len(redoList) == 2

    redoList.pop()
    undoList.append(lista)
    assert len(undoList) == 1
    assert len(redoList) == 1

    redoList.pop()
    undoList.append(lista)
    assert len(undoList) == 2
    assert len(redoList) == 0


