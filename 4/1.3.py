first = int(input('input first number'))
second = int(input('input second number'))

# так нравится больше
# print(max(first, second))
# print(min(first, second))

if first < second:
    print('max value', second)
    print('min value', first)
else:
    print('max value', first)
    print('min value', second)
