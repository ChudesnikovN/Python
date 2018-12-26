__author__ = 'Чудесников Никита'
# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

#easy2-2

def is_happy (number):
	number = str(number)
	i =0
	sum1 = 0
	sum2 = 0
	while i <= len(number) // 2 -1 :
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
		
print(is_happy(12310060))
print(is_happy(12321))
print(is_happy(436751))
