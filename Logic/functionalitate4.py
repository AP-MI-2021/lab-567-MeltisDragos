from Domain.cheltuiala import get_suma


def Ordonare_Descrescator_Dupa_Suma(lista):
    '''
    Ordoneaza cheltuielile in ordine descrescatoare dupa suma
    :return: lista modificata
    '''
    return sorted(lista, key=get_suma, reverse=True)
