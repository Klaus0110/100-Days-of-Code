def subarraySum(arr, n, sum):
    currentsum = arr[0]
    start = 0
    i = 1
    while i <= n:
        while currentsum > sum and start < i-1:
            currentsum = currentsum - arr[start]
            start += 1

        if currentsum == sum:
            print(f"Sum found between indexes {start} and {i-1}")
            return 1
        if i < n:
            currentsum = currentsum + arr[i]
        i += 1

    print("No subarray found")
    return 0


if __name__ == "__main__":
    n = int(input("Enter the number of elements in the array: "))
    a = []
    print("Enter the elements: ")
    for i in range(0, n):
        a.append(int(input()))
    s = int(input("Enter the sum to be found: "))
    subarraySum(a, n, s)