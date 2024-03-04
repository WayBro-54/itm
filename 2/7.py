import logging

logging.basicConfig(level=logging.INFO, filename='7_log.log')

print('input numbers')
try:
    str_lst = [int(i) for i in input().split()]
    print(sum(str_lst) / 2)

except ValueError:
    logging.error('value error, The numbers were expected')

