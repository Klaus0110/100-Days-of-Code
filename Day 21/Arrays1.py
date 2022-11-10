def mergearrays(arr1, arr2, n, m, arr3):
    i = 0
    j = 0
    k = 0
    while i < n:
        arr3[k] = arr1[i]
        i += 1
        k += 1
    while j < m:
        arr3[k] = arr2[j]
        j += 1
        k += 1
    arr3.sort()


if __name__ == '__main__':
    n1 = int(input("Enter the number of elements in array1: "))
    arr1 = []
    print("Enter the elements: ")
    for i in range(0, n1):
        arr1.append(int(input()))
    arr2 = []
    n2 = int(input("Enter the number of elements in array1: "))
    print("Enter the elements: ")
    for i in range(0, n2):
        arr2.append(int(input()))
    arr3 = [0 for i in range(n1+n2)]
    mergearrays(arr1, arr2, n1, n2, arr3)
    print("Arrays after merging: ")
    for i in range (n1+n2):
        print(arr3[i], end=" ")