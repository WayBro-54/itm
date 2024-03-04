
res = []

k = 0
for i in range(2, 51):
    for j in range(2, i):
        if i % j == 0:
            k += 1
    if k == 0:
        res.append(i)
    else:
        k = 0

print(res)
