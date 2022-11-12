def duplicates(arr, n):
    for i in range(n):
        arr[i] = arr[i] + 1

    res = []
    count = 0
    for i in range(n):

        if abs(arr[i]) > n:
            index = abs(arr[i]) // (n + 1)
        else:
            index = abs(arr[i])

        if index == n:
            count += 1
            continue

        val = arr[index]
        if val < 0:
            res.append(index - 1)
            arr[index] = abs(arr[index]) * (n + 1)
        elif val > n:
            continue
        else:
            arr[index] = -arr[index]

    if count > 1:
        res.append(n - 1)
    if len(res) == 0:
        res.append(-1)
    else:
        res.sort()
    return res


if __name__ == '__main__':
    num = int(input("Enter the number of elements in the array: "))
    a = []
    print("Enter the elements: ")
    for i in range(0, num):
        a.append(int(input()))
    ans = duplicates(a, num)
    print("Duplicates are: ")
    for i in ans:
        print(i)