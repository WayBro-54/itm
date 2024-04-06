import logging
import math

logging.basicConfig(level=logging.INFO, filename='5_log.log')

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    logging.info(f'succeed, x1={x1}, x2={x2})')
elif discr == 0:
    x = -b / (2 * a)
    logging.info(f'succeed, x1={x}')
else:
    logging.error(f'The equation has no solution')
