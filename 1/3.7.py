a, b, c = [int(i) for i in input().split()]

print(True if (a < b < c) or (c < b < a) else False)
