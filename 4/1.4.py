first = int(input('input first number: '))
second = int(input('input second number: '))
three = int(input('input three number: '))

if first < second:
    if first < three:
        print(first)
elif second < three:
    if second < first:
        print(second)
elif three < first:
    if three < second:
        print(three)
