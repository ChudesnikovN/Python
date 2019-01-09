__author__ = 'Чудесников Никита'

# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


from os import path as _path
from shutil import copy

filename = 'copy_' + _path.split(__file__)[1]
copy(__file__,filename)
