import sys
count = int(sys.stdin.readline())
for _ in range(count):
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    arr = [[0]*b for _ in range(a+1)]
    ans_sum = 0
    for i in range(a+1):
        for j in range(b):
            if i == 0:
                arr[0][j] = j+1
            else:
                arr[i][j] = sum(arr[i-1][k] for k in range(j+1))
    print(arr[a][b-1])