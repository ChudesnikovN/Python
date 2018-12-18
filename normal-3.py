__author__ = 'Чудесников Никита'

#normal-Задача 3

import math

print('Введите корни квадратного уравнения ax^2 + bx +c = 0')
a=int(input('Введите a: '))
b=int(input('Введите b: '))
c=int(input('Введите c: '))
s=str(a)+'x^2'+'+'+str(b)+'x'+'+'+str(c)+'=0'
print('Получилось уравнение: ',s)
D=(b**2 - 4*a*c)
if D >= 0:
	sqrtD = math.sqrt(b**2 - 4*a*c)
	x1 = (-sqrtD + b)/2
	x2 = (-sqrtD - b)/2
	print ('Его корни:')
	print('Корень 1 ',x1)
	print('Корень 2 ',x2)
else:
	print(' Нет корней ')

input()