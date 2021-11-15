from Domain.cheltuiala import get_nrapart


def sterge_toate_cheltuielile_dupa_apart(nrapart, lista):
    '''
    sterge toate cheltuielile pentru un apartament dat
    :param nrapart: numarul apartamentului
    :param lista: lista de cheltuieli
    :return: lista de cheltuieli fara cele ale apartamentului dat
    '''
    rezultat = []
    for cheltuiala in lista:
        if get_nrapart(cheltuiala) != nrapart:
            rezultat.append(cheltuiala)
    return rezultat