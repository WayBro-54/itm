# class Dog:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def __init__(self, name):
#         if not hasattr(self, 'name'):  # Проверяем, инициализирован ли атрибут name
#             self.name = name
#
#     def bark(self):
#         return f"{self.name} says woof!"
#
# # Пример использования
# dog1 = Dog("Rex")
# print(dog1.bark())  # Выведет: Rex says woof!
#
# dog2 = Dog("Max")
# print(dog2.bark())


class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
class Logger(metaclass=MetaSingleton):
    pass
logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)