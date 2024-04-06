# from functools import singledispatchmethod

class Calculator:

    def summ(self, a: int | float, b: int | float):
        return a + b


class Calcul(Calculator):

    def summ(self, a: str, b: str):
        return str(a) + str(b)


c = Calcul().summ(1, 3)
print(c)

