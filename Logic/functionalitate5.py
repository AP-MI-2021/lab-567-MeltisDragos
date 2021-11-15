from Domain.cheltuiala import get_data,get_suma

def Suma_Pe_Luna(lista):
    '''
    Returneaza suma pe luna
    :param lista:
    :return:
    '''
    rezultat = {}
    for cheltuiala in lista:
        data = get_data(cheltuiala).split(".")[1]
        pret = get_suma(cheltuiala)
        if data in rezultat:
            rezultat[data] = rezultat[data] + pret
        else:
            rezultat[data] = pret
    return rezultat
