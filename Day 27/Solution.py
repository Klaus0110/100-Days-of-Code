if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        command = input().split()
        cmd = command[0]
        if cmd != 'print':
            args = command[1:]
            command = f"arr.{cmd}({','.join(args)})"
            eval(command)
        else:
            print(arr)
