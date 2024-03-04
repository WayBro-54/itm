lst = ['a', 's', '1', 'a', '32', '23']

lst_dig = []
lst_asc = []


for i in lst:
    if i.isalpha():
        lst_asc.append(i)
    elif i.isdigit():
        lst_dig.append(i)

print(lst_dig, lst_asc)
