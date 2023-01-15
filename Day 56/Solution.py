from time import clock
MAX = 1000 
arr = [[0 for i in range(MAX)] for i in range(MAX)]
  
def rowMajor():
    global arr 
    # accessing element row wise
    for i in range(MAX):
        for j in range(MAX):
            arr[i][j] += 1
  
def colMajor():
    global arr
    # accessing element column wise
    for i in range(MAX):
        for j in range(MAX):
            arr[j][i] += 1
 
if __name__ == '__main__':
 
    # Time taken by row major order
    t = clock()
    rowMajor()
    t = clock() - t
    print("Row major access time :{:.2f} s".format(t))
 
    # Time taken by column major order
    t = clock()
    colMajor()
    t = clock() - t
    print("Column major access time :{:.2f} s".format(t))
