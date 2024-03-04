v = int(input())

estimation = {
    1: 'плохо',
    2: 'неудовлетворительно',
    3: 'удоавлетворительно',
    4: 'хорошо',
    5: 'отлично',
}

try:
    estimation[v]
except KeyError:
    raise KeyError('Invalid value')
else:
    print(estimation[v])
