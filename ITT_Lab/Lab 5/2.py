import numpy as np
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print("Enter the elements of the matrix row-wise:")
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
matrix = np.array(matrix)
print("\nTransposed Matrix:")
print( np.transpose(matrix))
