a, b = [int(i) for i in input().split()]

# print(True if (a % 2 == 1 and b % 2 == 0) elif (b % 2 == 1 and a % 2 == 0) else False)

if a % 2 == 1:
    if b % 2 == 0:
        print(True)
elif b % 2 == 1:
    if a % 2 == 0:
        print(True)
else:
    print(False)
