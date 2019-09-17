import random

from methods import bubble_sort

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(array)
print('before sort', array)
bubble_sort(array)
print('after sort', array)
