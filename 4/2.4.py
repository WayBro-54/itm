n, d = input().split()
# n - первоначальное направление , d - поворот

x = {
    (1, 'с'): 'север',
    (2, 'з'): 'запад',
    (3, 'ю'): 'юг',
    (4, 'в'): 'восток',
}

new_x = {
    0: 4,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 1,
}

napr = ()
for i in x.keys():
    if n == i[1]:  # текущее направление
        napr = i

new_napr = napr[0] + int(d)

for i in x.keys():
    j = new_x[new_napr]
    if i[0] == j:
        print(i)
