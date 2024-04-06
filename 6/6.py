class MeanOfTrans:

    def __init__(
        self,
        brand: str,
        color: str,
    ):
        self.brand = brand
        self.color = color

    # @property
    # def color(self):
    #     return self.__color
    #
    # @color.setter
    # def color(self, color):
    #     self.__color = color
    #
    # @property
    # def brand(self):
    #     return self.__brand
    #
    # @brand.setter
    # def brand(self, brand):
    #     self.__brand = brand


class Car(MeanOfTrans):
    def __init__(
            self,
            brand: str,
            color: str,
            number_of_wheels: int,
    ):
        super().__init__(brand, color)
        self.numbers_of_wheels = number_of_wheels


class Moped(MeanOfTrans):

    def __init__(
            self,
            brand: str,
            color: str,
            number_of_wheels: int,
    ):
        super().__init__(brand, color)
        self.number_of_wheels = number_of_wheels

    @staticmethod
    def get_time_of_the_distance(v, r):
        return f'{r / v} ч.'

    def __str__(self):
        return f'{self.brand}, {self.color}, {self.number_of_wheels}'


m = Moped(brand='honda', color='red', number_of_wheels=2)

print(m.get_time_of_the_distance(60, 500))
