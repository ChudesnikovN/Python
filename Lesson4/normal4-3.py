__author__ = 'Чудесников Никита'
# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random,os,re
os.chdir("C:\\geekbrains\\Python\\trashfolder")
_list = []
max_seq=[]

f= open ('numbs.txt', 'w', encoding='utf-8')
for i in range(2500):
	numb = str(random.randint(0,10))
	f.write(numb)
f.close()	

f= open ('numbs.txt', 'r', encoding='utf-8')
_str = f.read()
f.close()		

	
for i in range(0,10):
	pattern = r'[{}][{}]+'.format(i,i)
	_list += list(set(re.findall(pattern,_str)))

max_lenght = max (len(seq) for seq in _list)
max_seq = [seq for seq in _list if len(seq) == max_lenght]
print (max_seq)
