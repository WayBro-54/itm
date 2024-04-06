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
    car_drive = 4

    def __init__(
            self,
            brand: str,
            color: str,
            number_of_wheels: int,
    ):
        super().__init__(brand, color)
        self.numbers_of_wheels = number_of_wheels

    @classmethod
    def get_car_drive(cls):
        print(f'{cls.car_drive}')


# c = Car('honda', 'red', 4)

Car.get_car_drive()
