a, b, c = [float(i) for i in input().split()]

v = a * b * c

s = 2 * (a * b + b * c + a * c)

print(v, s)
