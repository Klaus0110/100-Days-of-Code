def getInvCount(arr, n):
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count


if __name__ == '__main__':
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    print("Enter the elements: ")
    for i in range(0, n):
        arr.append(int(input()))
    print("Number of inversions are", getInvCount(arr, n))