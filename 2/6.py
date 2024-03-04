import logging
import random

logging.basicConfig(level=logging.ERROR, filename='6_log.log')

MAX = 100
MIN = 5


def validate(min_num, max_num):
    if min_num < MIN or min_num > MAX:
        logging.error(f'the minimum value must be greater than {MIN}', exc_info=True)
        print(f'The minimum value must be greater than {MIN}')
        raise ValueError(f'The minimum value must be greater than {MIN}')

    if max_num > MAX or max_num < MIN:
        logging.error(f'the maximum value must be less than {MAX}')
        print(f'the maximum value must be less than {MAX}')
        raise ValueError(f'The maximum value must be less than {MAX}')


def input_():
    print('input min and max values for generate random number')
    min_num, max_num = [int(i) for i in input().split()]
    try:
        validate(min_num, max_num)
    except ValueError:
        min_num, max_num = input_()
    return min_num, max_num


def main():
    min_num, max_num = input_()
    validate(min_num, max_num)
    print(random.randint(min_num, max_num))


if __name__ == '__main__':
    main()

