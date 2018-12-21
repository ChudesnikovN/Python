__author__ = 'Чудесников Никита'
#Урок 2
#easy-Задача 2
import random
List1 = [random.randint(-100,100) for i in range(0,10)] # "Случайный список №1"
List2 = [random.randint(-100,100) for i in range(0,10)] # "Случайный список №1"
print(List1)
print(List2)
New_list = [i for i in List1 if i not in List2]
print(New_list)
input ()

