i = 2


def factoial(n):
    if n == 1:
        return n
    return n * factoial(n - 1)

print(factoial(5))
