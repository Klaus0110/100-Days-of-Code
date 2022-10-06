def fact(n):
    if (n==0):
        return 1
    elif(n<0):
        print("Invalid Number")
    elif(n>997):
        print("Number too large")
    else:
        return (n*fact(n-1))

n = int(input("Enter any number:"))
print(fact(n))
