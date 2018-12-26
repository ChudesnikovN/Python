__author__ = 'Чудесников Никита'
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
#normal3-4

def is_parallelogram (A1,A2,A3,A4):
	A1A2 = vector(A1,A2)
	A1A3 = vector(A1,A3)
	A1A4 = vector(A1,A4)
	A2A3 = vector(A2,A3)
	A2A4 = vector(A2,A4)
	A3A4 = vector(A3,A4)
	if ((parallel(A1A2,A3A4) and parallel(A2A3,A1A4) == True) or ( parallel(A1A3,A2A4) and parallel(A1A2,A3A4) == True)
		or (parallel(A1A4,A2A3) and parallel(A2A4,A1A3) == True)):
		return True
	else: 
		return False

def parallel (a,b):
	if b[1] == 0:
		if a[1] == 0:
			return True
		else:
			return False
	if b[0] == 0:
		if a[0] == 0:
			return True
		else:
			return False		
	if a[0]/b[0] == a[1]/b[1]:
		return True
	else:
		return False
		
def vector (Dot_A1, Dot_A2):
	vect =[]
	vect.insert(0,abs(Dot_A2[0] - Dot_A1[0]))
	vect.insert(1,abs(Dot_A2[1] - Dot_A1[1]))
	#print (vect)
	return vect
	
	
A2 = (2,2)
A3 = (4,5)
A1 = (8,6)
A4 = (6,3)

print (is_parallelogram(A1,A2,A3,A4))

A2 = (-2,-2)
A3 = (-2,2)
A1 = (2,2)
A4 = (2,-2)

print (is_parallelogram(A1,A2,A3,A4))

input()







