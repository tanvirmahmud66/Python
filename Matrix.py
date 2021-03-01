matrix = [
    [1,2,3],
    [4,5,6]
]
matrix[0][1] = 7
print(matrix[0][1])

for row in matrix:
    for col in row:
        print(col)