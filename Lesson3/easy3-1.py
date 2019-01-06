__author__ = 'Чудесников Никита'
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

#easy3-1

def my_round(number,n):
	int_n = int(n)
	stage = pow(10,int_n)
	mul = float(number)*stage
	result = int(mul)
	ost = mul-result
	if not (abs(ost) < 0.5):
		if result > 0: 
			result += 1
		else: 
			result -= 1
	return result/stage


number = input ('Введите число ')
n = input (' Введите количество знаков ')
print(my_round(number,n))