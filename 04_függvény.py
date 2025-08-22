
lista = [1434543, 345342, 335, 44353, 543535345, 435435346, 543535347,435538, 453459, 1657567657567560, 543535345, 435435346, 543535347, 435538, 435349, 165756765756756032]


def paros(lista):
    for i in lista:
        if i % 2 == 0:
            print(f"{i} páros szám")
        else:
            print(f"{i} páratlan szám")


def maximum(lista):
    for i in lista:
        if i == max(lista):
            print(f"{i} a legnagyobb szám a listában")

def minimum(lista):
    for i in lista:
        if i == min(lista):
            print(f"{i} a legkisebb szám a listában")

paros(lista)
maximum(lista)
minimum(lista)