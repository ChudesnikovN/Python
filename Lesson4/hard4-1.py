__author__ = 'Чудесников Никита'
#Пример. Дано:
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]
          
matrix_rotate = []

# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

matrix_rotate = [matrix [i][j] for i in range(0,len(matrix)) for j in range(0,len(matrix[i]))]
print (matrix_rotate)