__author__ = 'Чудесников Никита'
# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
#hard 3-1

import os

os.chdir("C:\\geekbrains\\Python\\trashfolder")

list_file = os.listdir()
i = 0
while i < len(list_file):
	os.remove(list_file[i])
	i += 1
	
with open ('C:\\geekbrains\\Python\\Homework\\fruits.txt', 'r') as f:
	for line in f:
		if line != '\n':
			letter = line[0]
			file_name = 'fruits_' + letter + '.txt'
			file = open(file_name, 'a', encoding='utf-8')
			file.write(line)
			file.close()