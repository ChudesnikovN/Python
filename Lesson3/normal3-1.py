__author__ = 'Чудесников Никита'
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
#normal 2-2

def fibbo (start, finish):
	row = []
	row.insert(0,1)
	row.insert(1,1)
	#print (row[1])
	i = 2
	while i <= finish:
		row.insert(i,row[i-1] + row[i-2])
		i += 1
	
	return(row[start-1:finish:])	

	
n = int(input('Введите начало '))
m = int(input('Введите конец '))
print (fibbo(n,m))
