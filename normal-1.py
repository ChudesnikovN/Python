__author__ = 'Чудесников Никита'

#normal-Задача 1

numb = int(input ('Введите число  '))
numb = abs(numb)
max = 0
while True:
	dig = numb % 10
	if dig > max:
		max=dig
	numb //= 10
	if numb == 0:
		break

print('Максимальная цифра в числе: ',max)
input()