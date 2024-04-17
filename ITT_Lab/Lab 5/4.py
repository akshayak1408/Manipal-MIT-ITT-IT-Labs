import numpy as np
n=int(input("enter the value of n"))
matrix1=[]
matrix2=[]
print("enter matrix1")
for i in range(0,n):
    row=[]
    row+=list(map(int,input().split(" ")))
    matrix1.append(row)
print("enter matrix2")
for i in range(0,n):
    row=[]
    row+=list(map(int,input().split(" ")))
    matrix2.append(row)
matrix1=np.array(matrix1)
matrix2=np.array(matrix2)
result=matrix1+matrix2
print(result)
