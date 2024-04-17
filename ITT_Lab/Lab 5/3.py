import numpy as np
n=int(input("enter the value of n"))
matrix1=[]
matrix2=[]
print("enter matrix1")
for i in range(0,n):
    row=[]
    row+=list(map(int,input("enter the row").split(" ")))
    matrix1.append(row)
print("enter matrix2")
for i in range(0,n):
    row=[]
    row+=list(map(int,input("enter the row").split(" ")))
    matrix2.append(row)
result=np.dot(matrix1,matrix2)
print(result)
