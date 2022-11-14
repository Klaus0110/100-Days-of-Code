def rotate(L, d, n):
    k = L.index(d)
    new_lis = []
    new_lis = L[k + 1:] + L[0:k + 1]
    return new_lis


if __name__ == '__main__':
    num = int(input("Enter the number of elements in the array: "))
    arr = []
    print("Enter the elements: ")
    for i in range(0, num):
        arr.append(int(input()))
    d = int(input("Enter the value of d: "))
    n = len(arr)

    # Function call
    arr = rotate(arr, d, n)
    for i in arr:
        print(i, end=" ")
