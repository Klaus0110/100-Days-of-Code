def checkneon(n):
    sq = n * n
    sum = 0
    while sq != 0:
        digit = sq % 10
        sum += digit
        sq = sq // 10
    return sum == n


number = int(input("Enter the number: "))
if checkneon(number):
    print(f"{number} is a neon number.")
else:
    print(f"{number} is not a neon number")
