a, b, o = [i for i in input().split()]
a, b = int(a), int(b)

operator = {
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a / b
}

res = operator[o](a, b)
print(res)
