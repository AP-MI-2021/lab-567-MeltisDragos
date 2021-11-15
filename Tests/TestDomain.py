from Domain.cheltuiala import creeaza_cheltuiala, get_id , get_nrapart , get_data , get_suma , get_tip


def test_cheltuiala():
    cheltuiala = creeaza_cheltuiala("1", 21, 179.59, "20.03.2002", "intretinere")
    assert get_id(cheltuiala) == "1"
    assert get_nrapart(cheltuiala) == 21
    assert get_data(cheltuiala) == "20.03.2002"
    assert get_suma(cheltuiala) == 179.59
    assert get_tip(cheltuiala) == "intretinere"
