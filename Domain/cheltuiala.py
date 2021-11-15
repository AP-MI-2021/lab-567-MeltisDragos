def creeaza_cheltuiala(id, nrapart,  suma, data, tip):
    '''
    Creeaza un dictionar pentru cheltuiala
    :param id: string
    :param nrapart: int
    :param suma: float
    :param data: string
    :param tip: string
    :return:
    '''
    return [id, nrapart, suma, data, tip]


def get_id(cheltuiala):
    '''
    id-ul unei cheltuieli
    :param cheltuiala: dictionar
    :return: id-ul cheltuielii
    '''
    return cheltuiala[0]


def get_nrapart(cheltuiala):
    '''
    numarul apartamentului unei cheltuieli
    :param cheltuiala: dictionar
    :return: numarul apartamentului cheltuielii
    '''
    return cheltuiala[1]


def get_suma(cheltuiala):
    '''
    suma unei cheltuieli
    :param cheltuiala: dictionar
    :return: suma cheltuielii
    '''
    return cheltuiala[2]


def get_data(cheltuiala):
    '''
    data unei cheltuieli
    :param cheltuiala: dictionar
    :return: data cheltuielii
    '''
    return cheltuiala[3]


def get_tip(cheltuiala):
    '''
    tipul unei cheltuieli
    :param cheltuiala: dictionar
    :return: tipul cheltuielii
    '''
    return cheltuiala[4]


def toString(cheltuiala):
    return "id: {}, nrapart: {}, suma: {}, data: {}, tip: {}".format(
        get_id(cheltuiala),
        get_nrapart(cheltuiala),
        get_suma(cheltuiala),
        get_data(cheltuiala),
        get_tip(cheltuiala),
    )
