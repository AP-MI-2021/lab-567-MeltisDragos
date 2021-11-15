from Domain.cheltuiala import get_data


def Adaugarea_Unei_Val_In_Suma(val, data1, lista):
    '''
    aduna o valoare la toate cheltuielile dintr-o dată citită
    :param val: valoarea care se aduna
    :param data1: data citita
    :param lista: lista de cheltuieli
    :return: lista de cheltuieli actualizata
    '''
    for cheltuiala in lista:
        if get_data(cheltuiala) == data1:
            cheltuiala[2] = cheltuiala[2]+val
    return lista

