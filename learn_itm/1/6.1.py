def binary_search(list, item):
  # в low и high хранятся границы части списка, где выполняется поиск
  low = 0
  high = len(list) - 1
  i = 0
  # Пока не останется один элемент
  while low <= high:
    # Проверяем средний элемент
    mid = (low + high) // 2
    guess = list[mid]
    # Значение найдено
    if guess == item:
      return mid
    # Значение велико
    if guess > item:
      high = mid - 1
    # Значение мало
    else:
      low = mid + 1
    i=i+1
    print(i)

  # Значение не найдено
  return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # => 1 (позиция элемента в списке)

# 'None' в Python означает "ничто". Элемент не найден.
print(binary_search(my_list, -1)) # => None