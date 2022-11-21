matrix = [[7,2,-3],
          [2,6, 5],
          [8,-4,3]]

# используем функцию из первой задачи
def maximum(x):
    listin = x
    m = listin[0]
    for i in range (len(listin)):
        if m < listin[i]:
            m = listin[i]
    return m 

def maximummatrix(z):
    matrix = z
    mm = matrix[0][0] # maximum in matrix
    for i in range(len(matrix)):
        c = maximum(matrix[i])
        if mm < c:
            mm = c
            
    return mm
        
print(maximummatrix(matrix))