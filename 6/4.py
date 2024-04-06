class MeanOfTrans:

    def __init__(
        self,
        brand: str,
        color: str,
    ):
        self.__brand = brand
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

