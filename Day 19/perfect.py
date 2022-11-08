number = int(input("Enter the number: "))
sum = 0
i = 1
while(i <= number/2):
    if(number % i == 0):
        sum += i
    i+=1
if(sum==number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")