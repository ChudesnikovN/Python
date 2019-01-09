

def change_dir (dirname):
	import os
	print (dirname)
	os.chdir(dirname)
	print('Успешно перешел в папку ' + dirname)
	
def list_directory ():
	import os
	_list = os.listdir()
	return _list
	
	
def remove_directory(dirname):
	import os
	os.rmdir(dirname)
	print('Успешно удалил папку '+ dirname)
	
def create_directory(dirname):
	import os
	os.mkdir(dirname)
	print('Успешно созадал папку ' + dirname)
	