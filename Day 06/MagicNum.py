import math

num = int(input("Enter a Number \n"))
digitCount = int(math.log10(num)) + 1
sumOfDigits = 0

temp = num

while (digitCount > 1):

    sumOfDigits = 0

    while (temp > 0):
        sumOfDigits += temp % 10
        temp = temp // 10

    temp = sumOfDigits

    digitCount = int(math.log10(sumOfDigits)) + 1

if (sumOfDigits == 1):
    print("Magic number")
else:
    print("Not a magic number")
