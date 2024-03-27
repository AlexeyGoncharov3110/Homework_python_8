# Задача_1:
# Напишите функцию для транспонирования матрицы

# def trans_matrix(matrix: list[int])-> list[int]:
#     trans_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

#     return trans_matrix


# print(trans_matrix([[2, 1, 31,], [3, 1, 51 ],[23,5,65],[32,5,67]]))



matrix = [[2, 1, 31,], [3, 1, 51 ],[23,5,65],[32,5,67]]
trans_matrix = [[0 for j in range(len (matrix))] for i in range(len (matrix[0]) )]
for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        trans_matrix[i][j] = matrix[j][i]
print(trans_matrix)
