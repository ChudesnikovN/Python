__author__ = 'Чудесников Никита'
__author__ = 'Чудесников Никита'
# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
#normal 3-3

import random

def my_filter (func,my_list):
	filtered_list =[]
	my_list = list(my_list)
	for i in range(0,len(my_list)):
		if func(my_list[i]) == True:
			filtered_list.insert(i,my_list[i])
			
	return filtered_list
	

def is_happy (number):
	number = str(number)
	i =0
	sum1 = 0
	sum2 = 0
	while i < len(number) // 2 -1 :
		sum1 += int(number[i])
		i += 1
	i =0
	while i <= len(number) // 2 -1 :
		sum2 += int(number[len(number)-1-i])
		i += 1
	if sum1 == sum2:
		return True
	else:
		return False

		
non_sorted = []		
for i in range(0,5):
	numb = random.randint(123456,1234567)
	non_sorted.append(numb)	
	
print(non_sorted)
print (my_filter(is_happy,non_sorted))

	