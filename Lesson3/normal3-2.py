__author__ = 'Чудесников Никита'
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
#normal3-2
import random

def my_sort(my_list):
	my_list = list(my_list)
	for j in range(0, len(my_list)-1):
		for i in range (0,len(my_list)-1-j):
			if my_list[i] > my_list[i+1]:
				my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
	
	return (my_list)
	

non_sorted = []
for i in range(0,10):
	numb = random.randint(-15,20)
	non_sorted.append(numb)
	
print(non_sorted)	
print(my_sort(non_sorted))


