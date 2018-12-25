# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

__author__ = 'Чудесников Никита'
#Урок 2
#norma2-4
import random
List1 = [random.randint(0,10) for i in range(0,10)]
List2 = list(List1)
print(List1)
New_list1 = list(set(List1))
print (New_list1)

j=0
New_list2 = []
for i in List2:
   if List2.count(i) == 1:
       New_list2.insert(i,i)
	   
	   
print (New_list2)
input ()