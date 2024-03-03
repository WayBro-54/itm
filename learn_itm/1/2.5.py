a, b = [int(i) for i in input().split()]

b_in_a = lambda a, b: a // b

print(a - b * b_in_a(a, b))
