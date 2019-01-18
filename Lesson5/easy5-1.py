__author__ = 'Чудесников Никита'
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
try:
    for i in range(1, 10):
        os.mkdir("dir_" + str(i))
except:
    print("Такая папка уже существует")
input('wait')

try:
    for i in range(1, 10):
        os.rmdir("dir_" + str(i))
except:
    print("Уже удалена")
	