__author__ = 'Чудесников Никита'
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

_list = [random.randint(-50,50) for x in range (100)]
_new_list =[]

_new_list = [numb for numb in _list if numb % 3 == 0 and numb >0 and numb % 4 !=0]
print (_list,' \n', _new_list)