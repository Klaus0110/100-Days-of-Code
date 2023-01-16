import math

def multiply(mat, res):
    N= len(mat)
    for i in range(0,N):
     
        for j in range(0,N):
         
            res[i][j] = 0
            for k in range(0,N):
                res[i][j] += mat[i][k] * mat[k][j]
 
def checkIdempotent(mat):
    N= len(mat)
    res =[[0]*N for i in range(0,N)]
    multiply(mat, res)
 
    for i in range(0,N):
        for j in range(0,N):    
            if (mat[i][j] != res[i][j]):
                return False
    return True
 
mat = [ [2, -2, -4],
        [-1, 3, 4],
        [1, -2, -3] ]

if (checkIdempotent(mat)):
    print("Idempotent Matrix")
else:
    print("Not Idempotent Matrix.")
