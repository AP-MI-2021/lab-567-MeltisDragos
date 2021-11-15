from Domain import cheltuiala
from Domain.cheltuiala import get_tip, get_suma


def Cea_Mai_Mare_Cheltuiala(lista):
    '''
    Determina cea mai mare cheltuiala pentru fiecare tip de cheltuială
    :param chel: tipul cheltuieli
    :param lista: lista de cheltuieli
    :return:
    '''
    max1 = 0
    for cheltuiala in lista:
        if "canal" == get_tip(cheltuiala):
            if get_suma(cheltuiala) > max1:
                max1 = cheltuiala[2]
    max2 = 0
    for cheltuiala in lista:
        if "intretinere" == get_tip(cheltuiala):
            if get_suma(cheltuiala) > max2:
                max2 = cheltuiala[2]
    max3 = 0
    for cheltuiala in lista:
        if "alte cheltuieli" == get_tip(cheltuiala):
            if get_suma(cheltuiala) > max3:
                max3 = cheltuiala[2]
    print(max1, max2, max3)



