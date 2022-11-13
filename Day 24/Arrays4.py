def findMissing(arr, N):
    temp = [0] * (N + 1)
    for i in range(0, N):
        temp[arr[i] - 1] = 1
    for i in range(0, N + 1):
        if temp[i] == 0:
            ans = i + 1
    print(ans)


# Driver code
if __name__ == '__main__':
    num = int(input("Enter the number of elements in the array: "))
    arr = []
    print("Enter the elements: ")
    for i in range(0, num):
        arr.append(int(input()))
    print("The misssing number is: ")
    findMissing(arr, num)