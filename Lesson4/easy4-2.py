__author__ = 'Чудесников Никита'
# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

_list1 = ['Манго', 'Папайя','Апельсин','Киви','Банан','Грейпфрут','Яблоко']
_list2 = ['Манго', 'Гранат','Помелло','Киви','Банан','Абрикос','Арбуз','Персик','Мандарин']

#первый вариант
_list_both = []

_list_both = list (set(_list1) & set(_list2))
print(_list_both)

#второй вариант:

_list_both = []

for fruit in _list1:
	if fruit in _list2:
		_list_both.append(fruit)
	
print(_list_both)