# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
od=OrderedDict()
n=int(input())
for i in range(n):
    m=input()
    od[m]=od.get(m,0)+1
print(len(od))
nj=[]
for _,i in od.items():
    nj.append(i)
print(*nj, sep=" ")
