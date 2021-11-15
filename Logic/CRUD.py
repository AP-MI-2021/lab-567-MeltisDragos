from Domain.cheltuiala import creeaza_cheltuiala, get_id


def Adauga_Cheltuiala(id, nrapart, suma, data, tip, lista):
    '''
    adauga o cheltuiala
    :param id:
    :param nrapart:
    :param suma:
    :param data:
    :param tip:
    :param lista: lista cheltuielilor
    :return: o list cu cheltuielile
    '''
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    if data.count('.') != 2 or data.split(".")[0].isnumeric() == False or data.split(".")[1].isnumeric() == False or data.split(".")[2].isnumeric() == False:
        raise ValueError("Ati bagat data gresita!")
    else:
        if(data.split(".")[1] == "01" or data.split(".")[1] == "03" or data.split(".")[1] == "05" or data.split(".")[1] == "07" or data.split(".")[1] == "08" or data.split(".")[1] == "10" or data.split(".")[1] == "12") and int(data.split(".")[0]) > 31:
            raise ValueError("Ati bagat data gresita!")
        if (data.split(".")[1] == "04" or data.split(".")[1] == "06" or data.split(".")[1] == "09" or data.split(".")[1] == "11") and int(data.split(".")[0]) > 30:
            raise ValueError("Ati bagat data gresita!")
        if data.split(".")[1] == "02" and int(data.split(".")[2]) % 4 == 0 and int(data.split(".")[0]) > 29:
            raise ValueError("Ati bagat data gresita!")
        if data.split(".")[1] == "02" and int(data.split(".")[2]) % 4 != 0 and int(data.split(".")[0]) > 28:
            raise ValueError("Ati bagat data gresita!")
        if int(data.split(".")[1]) > 12:
            raise ValueError("Ati bagat data gresita!")
    if tip != "canal" and tip != "intretinere" and tip !="alte cheltuieli":
        raise ValueError("Ati bagat tip-ul gresit")
    cheltuiala = creeaza_cheltuiala(id, nrapart, suma, data, tip)
    return lista + [cheltuiala]


def getById(id, lista):
    '''
    da elementul cu id-ul dat
    :param id:
    :param lista:
    :return:cheltuiala cu id-ul dat sau None, daca nu exista cheltuiala cu id-ul dat
    '''
    if id.isnumeric() == False:
        raise ValueError("Id-ul trebuie sa fie format din cifre!")
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            return cheltuiala
    return None


def stergere_cheltuiala(id, lista):
    '''
    sterge o cheltuiala
    :param id:
    :param lista:
    :return: lista fara cheltuiala cu id-ul dat
    '''
    if getById(id, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu id-ul dat!")
    return [cheltuiala for cheltuiala in lista if get_id(cheltuiala) != id]


def modificare_cheltuiala(id, nrapart, suma, data, tip, lista):
    '''
    modifica o cheltuiala dintr-o listadata
    :param id:
    :param lista: o lista cu cheltuieli
    :return: lista modificata
    '''
    if getById(id, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu id-ul dat!")
    listaNoua = []
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            cheltuiala_noua = creeaza_cheltuiala(id, nrapart, suma, data, tip)
            listaNoua.append(cheltuiala_noua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua



