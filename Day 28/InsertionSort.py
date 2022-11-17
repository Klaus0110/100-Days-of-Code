# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Driver code to test above
if __name__ == '__main__':
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    print("Enter the elements: ")
    for i in range(0, n):
        arr.append(int(input()))
    insertionSort(arr)
    print("After Sorting: ")
    for i in range(len(arr)):
        print("% d" % arr[i])