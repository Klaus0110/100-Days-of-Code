print("Enter the Number of Rows: ", end="")
row = int(input())
if(row<=0):
    print("Enter a positive value!")
else:
    num = 1
    i = 0
    while i < row:
        j = 0
        while j < i+1:
            print(num, end=" ")
            num = num+1
            j = j+1
        print()
        i = i+1