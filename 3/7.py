lst = [1,2,3,4,5,6,7,8,9,10,11]

for i in lst:
    print(i)

for i, v in {i: i*i for i in lst}.items():
    print('ключ:', i, 'значение:', v)
