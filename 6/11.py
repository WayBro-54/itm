from abc import ABC, abstractmethod


class Animals(ABC):
    @abstractmethod
    def voice(self):
        '''
        Звук издаваемый животным
        '''


class Cat(Animals):

    def voice(self):
        return 'Мяу'


class Dog(Animals):

    def voice(self):
        return 'гав'


animals = Dog().voice()

print(animals)
