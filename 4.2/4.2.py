#Задание 1

import random

def new_matrix(row, col):
    matrix = []
    for _ in range(row):
        row = []
        for _ in range(col):
            row.append(random.randint(-100, 100))
        matrix.append(row)
    return matrix

def summ(matrix_1, matrix_2):
    row = len(matrix_1)
    col = len(matrix_1[0])
    result = []
    for a in range(row):
        row = []
        for b in range(col):
            summ_value = matrix_1[a][b] + matrix_2[a][b]
            row.append(summ_value)
        result.append(row)
    return result

matrix_1 = new_matrix(10, 10)

matrix_2 = new_matrix(10, 10)

matrix_3 = summ(matrix_1, matrix_2)

print("Первая матрица:")
for row in matrix_1:
    print(row)

print("Вторая матрица:")
for row in matrix_2:
    print(row)

print("Результат:")
for row in matrix_3:
    print(row)