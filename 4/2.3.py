d, m = [int(i) for i in input().split()]

x = {
    1: ('Январь', 31),
    2: ('Февраль', 28),
    3: ('Март', 31),
    4: ('Апрель', 30),
    5: ('Май', 31),
    6: ('Июнь', 30),
    7: ('Июль', 31),
    8: ('Август', 31),
    9: ('Сентябрь', 30),
    10: ('Октябрь', 31),
    11: ('Ноябрь', 30),
    12: ('Декабрь', 31),
}


mes = x[m]
if mes[1] == d:
    print(1, m + 1)
else:
    print(d + 1, m)