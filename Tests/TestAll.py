from Tests.TestCRUD import test_Adauga_Cheltuieli, test_stergere_cheltuiala, test_undo_redo
from Tests.TestDomain import test_cheltuiala



def runAllTests():
    test_cheltuiala()
    test_Adauga_Cheltuieli()
    test_stergere_cheltuiala()
    test_undo_redo()