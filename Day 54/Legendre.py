def largestPower(n, p):
     
    x = 0
 
    while n:
        n /= p
        x += n
    return x
 
# Driver program
n = int(input("Enter the value of n: "))
p = int(input("Enter the value of p: "))
print ("The largest power of %d that divides %d! is %d\n"%(p, n, largestPower(n, p)))
