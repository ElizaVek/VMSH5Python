'''Проверить, равны ли суммы чисел во всех строках
и столбцах матрицы
Заданная матрица:
[[8, 1, 6], [3, 5, 7], [4, 9, 2]]
Выходные данные:
YES'''

Matrix = [[8, 1, 6],
          [3, 5, 7],
          [4, 9, 2]]

answer = 'YES'

s = 0
for i in range(len(Matrix[0])):
    s += Matrix[0][i]
    
for j in range(len(Matrix)):   
    ss = 0
    for i in range(len(Matrix[0])):
        ss += Matrix[j][i]
    if s != ss:
        answer = 'NO'
        
for i in range(len(Matrix[0])):
    ss = 0
    for j in range(len(Matrix)):
        ss += Matrix[j][i]
    if s != ss:
        answer = 'NO'
        
print(answer)